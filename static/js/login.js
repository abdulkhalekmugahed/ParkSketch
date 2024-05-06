// login.js

// Function to check if a string is empty or contains only whitespace
function isEmpty(str) {
    return str.trim() === "";
}

// Function to validate an email address
function validateEmail(email) {
    // Regular expression for email validation
    var re = /\S+@\S+\.\S+/;
    return re.test(email);
}

//  Function to validate the login form
function validateLoginForm() {
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;

    if (isEmpty(email)) {
        alert("Please enter your email address.");
        return false;
    }

    if (!validateEmail(email)) {
        alert("Please enter a valid email address.");
        return false;
    }

    if (isEmpty(password)) {
        alert("Please enter your password.");
        return false;
    }

    // Validation passed
    return true;
}