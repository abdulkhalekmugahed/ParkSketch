// signup.js

// Function to check if a string is empty or contains only whitespace
function isEmpty(str) {
    return str.trim() === '';
}

// Function to validate an email address
function validateEmail(email) {
    // Regular expression for email validation
    var re = /\S+@\S+\.\S+/;
    return re.test(email);
}

// Function to check password strength
function checkPasswordStrength(password) {
    // At least one lower case letter, one upper case letter, one digit, one special character, and at least 8 characters long
    var re = /^(?=.*\d)(?=.*[!@#$%^&*])(?=.*[a-z])(?=.*[A-Z]).{8,}$/;
    return re.test(password);
}

// Function to validate the signup form
function validateForm() {
    var name = document.getElementById('name').value;
    var email = document.getElementById('email').value;
    var password = document.getElementById('password').value;

    if (isEmpty(name)) {
        alert('Please enter your name.');
        return false;
    }

    if (isEmpty(email)) {
        alert('Please enter your email address.');
        return false;
    }

    if (!validateEmail(email)) {
        alert('Please enter a valid email address.');
        return false;
    }

    if (isEmpty(password)) {
        alert('Please enter your password.');
        return false;
    }

    if (!checkPasswordStrength(password)) {
        alert('Password must be at least 8 characters long and contain a lowercase letter, an uppercase letter, a digit, and a special character.');
        return false;
    }

    return true; // Form is valid
}

