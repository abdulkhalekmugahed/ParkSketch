# Import necessary modules
import numpy as np  # For numerical operations
import os  # For interacting with the operating system
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
from keras.models import load_model  # For loading Keras models
from keras.preprocessing.image import load_img, img_to_array  # For image preprocessing
import pyrebase  # For interacting with the Firebase platform
from flask import Flask, redirect, render_template, request, session, url_for  # For web application development using Flask
from datetime import datetime  # For working with date and time
import re  # For regular expressions

# Create a new Flask application
app = Flask(__name__)
# Set the secret kep for the Flask app. This is used for session security.
app.secret_key = "0101010"

# Configuration for Firebase
config = {
    'apiKey': 'AIzaSyDZo472sANtS8I46z0_AxGMm7CTOMmoesM',
    'authDomain': 'parksketch-01.firebaseapp.com',
    'projectId': 'parksketch-01',
    'storageBucket': 'parksketck-01.appspot.com',
    'messagingSenderId': '428838688775',
    'appId': '1:428838688775:web:6af1acdb251207ef5372a2',
    'databaseURL': 'https://parksketch-01-default-rtdb.firebaseio.com'
}

# Initialize Firebase
firebase = pyrebase.initialize_app(config)

# Get reference to the auth service and database service
auth = firebase.auth()
db = firebase.database()


# Route for the login page
@app.route("/")
@app.route("/home")
def login():
    return render_template("login.html")


# Route for the signup page
@app.route("/signup")
def signup():
    return render_template("signup.html")


# Route for the diagnosis page
@app.route("/diagnosis")
def diagnosis():
    # Check if user is logged in
    if session.get("is_logged_in", False):
        return render_template("diagnosis.html", email=session["email"], name=session["name"])
    else:
        # If user is not logged in, redirect to login page
        return redirect(url_for('login'))


# Function to check password strength
def check_password_strength(password):
    # At least one lower case letter, one upper case letter, one digit, one special character, and at least 8 characters long
    return re.match(r'^(?=.*\d)(?=.*[!@#$%^&*])(?=.*[a-z])(?=.*[A-Z]).{8,}$', password) is not None


# Route for login result
@app.route("/result", methods=["POST", "GET"])
def result():
    if request.method == "POST":
        result = request.form
        email = result["email"]
        password = result["pass"]
        try:
            # Authenticate user
            user = auth.sign_in_with_email_and_password(email, password)
            session["is_logged_in"] = True
            session["email"] = user["email"]
            session["uid"] = user["localId"]
            # Fetch user data
            data = db.child("users").get().val()
            # Update session data
            if data and session["uid"] in data:
                session["name"] = data[session["uid"]]["name"]
                # Update last login time
                db.child("users").child(session["uid"]).update(
                    {"last_logged_in": datetime.now().strftime("%m/%d/%Y, %H:%M:%S")})
            else:
                session["name"] = "User"
            # Redirect to diagnosis page
            return redirect(url_for('diagnosis'))
        except Exception as e:
            print("Error occurred: ", e)
            error_message = "Invalid email address or password. Please try again."
            return render_template("login.html", error=error_message)
    else:
        # If user is logged in, redirect to diagnosis page
        if session.get("is_logged_in", False):
            return redirect(url_for('diagnosis'))
        else:
            return redirect(url_for('login'))


# Route for user registration
@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        result = request.form
        email = result["email"]
        password = result["pass"]
        name = result["name"]
        if not check_password_strength(password):
            print("Password does not meet strength requirements")
            return redirect(url_for('signup'))
        try:
            # Create user account
            auth.create_user_with_email_and_password(email, password)
            # Authenticate user
            user = auth.sign_in_with_email_and_password(email, password)
            session["is_logged_in"] = True
            session["email"] = user["email"]
            session["uid"] = user["localId"]
            session["name"] = name
            # Save user data
            data = {"name": name, "email": email, "last_logged_in": datetime.now().strftime("%m/%d/%Y, %H:%M:%S")}
            db.child("users").child(session["uid"]).set(data)
            return redirect(url_for('diagnosis'))
        except Exception as e:
            print("Error occurred during registration: ", e)
            error_message = "The email address already exists in another account."
            return render_template("signup.html", error=error_message)

    else:
        # If user is logged in, redirect to diagnosis page
        if session.get("is_logged_in", False):
            return redirect(url_for('diagnosis'))
        else:
            return redirect(url_for('signup'))


# Route for password reset
@app.route("/reset_password", methods=["GET", "POST"])
def reset_password():
    if request.method == "POST":
        email = request.form["email"]
        try:
            # Send password reset email
            auth.send_password_reset_email(email)
            # Show a page telling user to check their email
            return render_template("reset_password_done.html")
        except Exception as e:
            print("Error occurred: ", e)
            error_message = "An error occurred. Please try again."
            return render_template("reset_password.html", error=error_message)
    else:
        return render_template("reset_password.html")


# Route for logout
@app.route("/logout")
def logout():
    # Update last logout time
    db.child("users").child(session["uid"]).update({"last_logged_out": datetime.now().strftime("%m/%d/%Y, %H:%M:%S")})
    session["is_logged_in"] = False
    return redirect(url_for('login'))


# Load the trained model
model_path = 'custom_densenet_model.h5'
model = load_model(model_path)


def predict_image(img_path, model):
    """
    Predict the label of an image using a given model 
    Parameters:
        img_path (str): The file path of the image to be predicted.
        model (keras.Model): The trained Keras model used for prediction.

    Returns:
         str: The predicted label ('Healthy' or 'Parkinson').
    """
    # Load the image from the given path and resize it to the target size
    img = load_img(img_path, target_size=(224, 224))
    # Convert the image to an array
    img_tensor = img_to_array(img)
    # Expand the dimensions to match the expected input shape of the model
    img_tensor = np.expand_dims(img_tensor, axis=0)
    # Normalize the image pixel values
    img_tensor /= 255.
    # Make predictions using the provided model
    prediction = model.predict(img_tensor)
    # Retrieve the predicted probability of the positive class
    predicted_pro = prediction[0]
    # Define a dictionary mapping class indices to class labels
    class_mapping = {0: 'Healthy', 1: 'Parkinson'}
    # Define the threshold for binary classification
    threshold = 0.5
    # Determine the predicted class based on the threshold
    if predicted_pro >= threshold:
        predicted_class = 1
    else:
        predicted_class = 0
    # Retrieve the predicted label based on the predicted class
    predicted_label = class_mapping[predicted_class]

    return predicted_label


# Route for handling image upload and making predictions
@app.route('/predict', methods=['POST'])
def upload():
    # Check if the request method is POST
    if request.method == 'POST':
        # Retrieve the uploaded file from the request
        file = request.files['file']
        # Save the file to the server's ./uploads directory
        base_path = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(base_path, 'uploads', file.filename)
        file.save(file_path)
        # Make prediction using the uploaded image and the trained model
        result = predict_image(file_path, model)
        # Get the user ID from the session
        user_id = session.get("uid")
        # Prepare prediction data to be stored in the database
        prediction_data = {
            "result": result,
            "image_file_name": file.filename,
            "timestamp": datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),
        }
        # Store prediction data in the Firebase database under the user's ID
        db.child("users").child(user_id).child("predictions").push(prediction_data)

        # Return the prediction result as the response
        return result

    # If the request method is not POST, return None
    return None


# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True, port=5002)
