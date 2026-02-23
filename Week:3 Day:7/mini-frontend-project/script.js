// Home Page Button
function welcomeMessage() {
    alert("Welcome to Our Website!");
}

// Registration Validation
let registerForm = document.getElementById("registerForm");
if (registerForm) {
    registerForm.addEventListener("submit", function(event) {
        let name = document.getElementById("regName").value;
        let email = document.getElementById("regEmail").value;
        let password = document.getElementById("regPassword").value;

        if (name === "" || email === "" || password === "") {
            alert("All fields are required!");
            event.preventDefault();
        } else {
            alert("Registration Successful!");
        }
    });
}

// Login Validation
let loginForm = document.getElementById("loginForm");
if (loginForm) {
    loginForm.addEventListener("submit", function(event) {
        let email = document.getElementById("loginEmail").value;
        let password = document.getElementById("loginPassword").value;

        if (email === "" || password === "") {
            alert("Please fill all fields!");
            event.preventDefault();
        } else {
            alert("Login Successful!");
        }
    });
}

// Contact Form Validation
let contactForm = document.getElementById("contactForm");
if (contactForm) {
    contactForm.addEventListener("submit", function(event) {
        let name = document.getElementById("contactName").value;
        let message = document.getElementById("contactMessage").value;

        if (name === "" || message === "") {
            alert("Please fill all fields!");
            event.preventDefault();
        } else {
            alert("Message Sent Successfully!");
        }
    });
}
