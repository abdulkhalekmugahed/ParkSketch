# ParkSketch: Early Diagnosis of Parkinson’s Disease Using Hand-Drawn Images

**ParkSketch** is an AI-powered web application designed to diagnose Parkinson's Disease (PD) through the analysis of hand-drawn images, specifically spirals and waves. Leveraging cutting-edge deep learning techniques, including convolutional neural networks (CNNs) and transfer learning, this project aims to facilitate early diagnosis, significantly enhancing patient care and management.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation and Usage](#installation-and-usage)
  - [Prerequisites](#prerequisites)
  - [Setup Instructions](#setup-instructions)
  - [Running the Application](#running-the-application)
- [Model Performance](#model-performance)
- [Screenshots](#screenshots)
  - [Login Page](#1-login-page)
  - [Sign Up Page](#2-sign-up-page)
  - [Reset Password Page](#3-reset-password-page)
  - [Reset Password Done Page](#4-reset-password-done-page)
  - [Diagnosis Page](#5-diagnosis-page)
  - [Email Address Validation](#6-email-address-validation)
  - [Password Strength Validation](#7-password-strength-validation)
  - [Invalid Login Credentials](#8-invalid-login-credentials)
  - [Existing User Registration](#9-existing-user-registration)
  - [Password Reset Without Email](#10-password-reset-without-email)
  - [Password Reset with Email](#11-password-reset-with-email)
  - [Image Upload](#12-image-upload)
  - [View Result](#13-view-result)
  - [Firebase Realtime Database](#14-firebase-realtime-database)
  - [Accuracy and Loss Curves](#15-accuracy-and-loss-curves-training-and-validation)
  - [Loss and Test Accuracy](#16-loss-and-test-accuracy)
  - [Confusion Matrix](#17-confusion-matrix)
  - [Classification Report](#18-classification-report)
  - [Area Under Curve](#19-area-under-curve)
- [How It Works](#how-it-works)
- [Future Work](#future-work)
- [Project Demo](#project-demo)
- [License](#license)

## Overview

Parkinson’s Disease, also widely known as **shaking paralysis**, is one of the most common brain disorders. It is a **progressive neurodegenerative disease**, meaning it worsens over time. It is considered neurodegenerative because certain neurons in the brain become damaged, particularly in a part of the midbrain called the **substantia nigra**. These damaged neurons produce **dopamine**, a vital neurotransmitter that allows us to perform smooth and balanced movements. As dopamine levels decrease, various **motor and non-motor symptoms** appear, which differ from person to person.

Motor symptoms include **rigidity, slowness of movement, difficulties with walking and balance**, and **tremors** in the limbs or head, which may also be accompanied by **sleep disorders**.

Since no cure eliminates the disease, **early diagnosis** of Parkinson’s Disease, along with appropriate treatment, can help alleviate the symptoms and improve the patient's quality of life.

However, early diagnosis of Parkinson’s presents a challenge for doctors, as its symptoms are similar to those of other neurodegenerative disorders.

Recent studies have indicated that patients with Parkinson’s exhibit **handwriting changes** compared to healthy individuals. Based on these findings, it is possible to develop systems for the **diagnosis, follow-up, and monitoring** of patients. **ParkSketch** addresses this challenge by utilizing handwriting analysis as a diagnostic tool, offering a novel and accessible solution.

## Features

- **High Accuracy**: The model achieved an accuracy of 99.54%, a precision of 99.69%, a recall of 99.39%, an F1-score of 99.54%, and a perfect Area Under the Curve (AUC) of 100%.
- **User-Friendly Web Interface**: Patients can easily upload hand-drawn images for analysis and receive immediate feedback on their diagnosis.
- **Secure Database**: Results are stored securely, allowing healthcare professionals to monitor the progression of Parkinson's Disease (PD) over time.
- **User Registration**: New users can easily create their accounts.
- **User Authentication**: Existing users can log into their accounts securely.
- **Session Management**: The application maintains user sessions, keeping users signed in.
- **Password Reset**: Users can easily reset forgotten passwords.
- **Firebase Integration**: The application integrates with Firebase for back-end services, ensuring efficient data management.
- **Security**: Passwords are securely managed, and sessions are handled properly to mitigate common security issues.

## Technologies Used

- **Backend**: Python (TensorFlow, Keras, Flask)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: Firebase Realtime Database
- **Other Libraries**: OpenCV, Scikit-Learn, NumPy, Pandas, Matplotlib, Seaborn
  
## Installation and Usage

### Prerequisites

Before you start, you need to have the following:

- **Python** (Version 3.6 or above)
- **Keras**
- **Flask**
- **Pyrebase** (A Python wrapper for the Firebase API)
- **Firebase account** (to set up the back-end services)

### Setup Instructions

Follow these steps to get the application running:

1. **Clone this repository to your local machine.**
    ```bash
    git clone https://github.com/abdulkhalekmugahed/ParkSketch
    ```

2. **Navigate into the project directory.**
    ```bash
    cd ParkSketch
    ```

3. **Install the required packages.**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up your Firebase project:**
    - Navigate to the [Firebase Console](https://console.firebase.google.com/).
    - Create a new Firebase project.
    - Under "Your Apps" in "Project Settings," select the "Config" radio button to get your Firebase SDK config.
    - Replace the "config" variables in `router.py` with your own Firebase project credentials. It should look like this:
    ```python
    config = {
        'apiKey': '<your-api-key>',
        'authDomain': '<your-auth-domain>',
        'projectId': '<your-project-id>',
        'storageBucket': '<your-storage-bucket>',
        'messagingSenderId': '<your-messaging-sender-id>',
        'appId': '<your-app-id>',
        'databaseURL': '<your-database-url>'

    }
    ```

    - Enable the Firebase Realtime Database by clicking on **Realtime Database** in the left panel, and adjust the rules setting to enable read and write access:
    ```json
    {
      "rules": { ".read": true, ".write": true }
    }
    ```

### Running the Application

To start the application, execute the following command in your terminal:

```bash
python router.py
```

## Model Performance

- **Accuracy**: 99.54%
- **Precision**: 99.69%
- **Recall**: 99.39%
- **F1-score**: 99.54%
- **AUC**: 100%

## Screenshots

### 1. Login Page  
<div> 
    <img src="https://github.com/user-attachments/assets/d9c42927-2f05-4ce9-adc2-b8e69ba5368b" alt="Login Page" width="800">
</div>

### 2. Sign Up Page  
<div>
    <img src="https://github.com/user-attachments/assets/053e6812-8aae-4298-a064-225b29203127" alt="Sign Up Page" width="800">
</div>

### 3. Reset Password Page  
<div>
    <img src="https://github.com/user-attachments/assets/0b9f071b-3921-4be2-8ad6-e1eb9abcfefd" alt="Reset Password Page" width="800">
</div>

### 4. Reset Password Done Page  
<div>
    <img src="https://github.com/user-attachments/assets/8cbff005-1d57-482f-bcac-06d2443dab0f" alt="Reset Password Done Page" width="800">
</div>

### 5. Diagnosis Page  
<div>
    <img src="https://github.com/user-attachments/assets/748c8399-2055-4933-9fbf-749d0fba47c7" alt="Diagnosis Page" width="800">
</div>

### 6. Email Address Validation  
Verify the system's response to an invalid email during sign-up.
<div>
    <img src="https://github.com/user-attachments/assets/8e5a19ba-a38b-4645-927c-80b9960c4f5a" alt="Email Address Validation" width="800">
</div>

### 7. Password Strength Validation  
Check the response to a weak password during sign-up.
<div>
    <img src="https://github.com/user-attachments/assets/3e657f82-ed39-414d-899d-7444dd5af6c3" alt="Password Strength Validation" width="800">
</div>

### 8. Invalid Login Credentials  
Test login with incorrect credentials.
<div>
    <img src="https://github.com/user-attachments/assets/43fcd5c7-df23-486d-8684-c8753388d9d3" alt="Invalid Login Credentials" width="800">
</div>

### 9. Existing User Registration  
Test the response when an existing user attempts registration.
<div>
    <img src="https://github.com/user-attachments/assets/2f21dbb3-81d1-41e0-9acf-d97ace411ded" alt="Existing User Registration" width="800">
</div>

### 10. Password Reset Without Email  
Verify password reset without email input.
<div>
    <img src="https://github.com/user-attachments/assets/b36e163f-4243-4442-8a3b-c35b8e516938" alt="Password Reset Without Email" width="800">
</div>

### 11. Password Reset with Email  
Verify email-based password reset process.
<div>
    <img src="https://github.com/user-attachments/assets/6ff3ada6-3296-457d-b35c-c72921d9fbc2" alt="Password Reset with Email" width="800">
</div>

### 12. Image Upload  
Test the ability to upload hand-drawn images.
<div>
    <img src="https://github.com/user-attachments/assets/832e608e-baae-4444-8d82-8fc969060e75" alt="Image Upload" width="800">
</div>

### 13. View Result  
Verify the display of the model’s predicted result.
<div>
    <img src="https://github.com/user-attachments/assets/e959a7b5-2683-4c16-a0f9-f0324c64c4db" alt="View Result" width="800">
</div>

### 14. Firebase Realtime Database  
<div>
    <img src="https://github.com/user-attachments/assets/db190ffd-61d3-47e8-aa66-65ae3d78bc9d" alt="Firebase Realtime Database" width="800">
</div>

### 15. Accuracy and Loss Curves (Training and Validation)  
<div>
    <img src="https://github.com/user-attachments/assets/9a790b3e-3cfd-479f-9840-8356c2ef012a" alt="Accuracy and Loss Curves" width="500">
</div>

### 16. Loss and Test Accuracy  
<div>
    <img src="https://github.com/user-attachments/assets/656c25cb-7bba-45e3-a9da-d783edf20514" alt="Loss and Test Accuracy" width="500">
</div>

### 17. Confusion Matrix  
<div>
    <img src="https://github.com/user-attachments/assets/81ea4337-0799-4f49-8270-6f327c81aa4d" alt="Confusion Matrix" width="500">
</div>

### 18. Classification Report  
<div>
    <img src="https://github.com/user-attachments/assets/36192f92-0905-44bc-adc4-c9a6c0b64884" alt="Classification Report" width="500">
</div>

### 19. Area Under Curve  
<div>
    <img src="https://github.com/user-attachments/assets/c011be7e-9256-40a1-98b1-1b8bd43c3593" alt="Area Under Curve" width="500">
</div>


## How It Works  

1. **User Registration/Login**:  
   - New users create an account by providing their email and setting a password.  

2. **Image Upload**:  
   - Users upload hand-drawn images (spirals or waves) through the web interface.  

3. **Image Preprocessing**:  
   - The uploaded images are preprocessed using **Keras** to extract relevant features.  
   - Techniques such as **resizing** and **normalization** prepare the images for model prediction.

4. **Model Prediction**:  
   - The custom pre-trained **DenseNet201** model analyzes the preprocessed images.  
   - It classifies the input as either 'Healthy' or 'Parkinson' by leveraging high feature extraction accuracy.

5. **Results Display**:  
   - The diagnosis result ('Healthy' or 'Parkinson') is displayed instantly on the web interface.  

6. **Data Storage**:  
   - The result, along with the name of the uploaded image and user information, is securely stored in the **Firebase Realtime Database**.  
   - Healthcare professionals can monitor the patient's diagnosis history over time, facilitating better tracking and follow-up.

7. **Profile Management and Session Handling**:  
   - Session management ensures users stay logged in until they manually log out or the session expires.

8. **Password Reset**:  
   - If users forget their password, they can reset it by entering their registered email address.  
   - A password reset link is sent via email, enabling users to regain access quickly and securely.  


## Future Work

ParkSketch has achieved promising results in differentiating between Parkinson's Disease (PD) and healthy cases using hand-drawn sketches. However, several areas for further exploration could enhance its capabilities and impact:

- **Incorporation of Additional Data Sources**:  
  Integrating additional data sources, such as MRI data for Substantia nigra analysis, has the potential to improve the accuracy and reliability of ParkSketch's diagnostic capabilities. This incorporation would provide a more holistic understanding of Parkinson's Disease, potentially leading to even more accurate diagnoses.

- **Enhanced Usability**:  
  Ensuring that ParkSketch's user interface is responsive across various screen sizes and devices is crucial for accessibility. Healthcare professionals can seamlessly access and utilize the system on desktops, tablets, and mobile devices by optimizing the interface design.

- **Validation and Clinical Integration**:  
  Conducting comprehensive validation studies and clinical trials to assess ParkSketch's real-world performance and effectiveness is another important area for future work. Collaborating with healthcare institutions and research organizations will provide valuable insights, enabling refinement and optimization to meet clinical standards.

- **Continuous Improvement**:  
  Implementing a system for continuous monitoring, evaluation, and optimization of ParkSketch is vital for long-term effectiveness. Regular updates based on user feedback, technological advancements, and emerging research will ensure the system remains accurate, user-friendly, and clinically relevant.


## Project Demo

Check out the live demo of the project [here](https://drive.google.com/file/d/1NQCo8AFtEwljV1grdsg_1j_OAdURsjRj/view?usp=sharing#).  

## License

```
Copyright 2024 Abdulkhalek Mugahed

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```


