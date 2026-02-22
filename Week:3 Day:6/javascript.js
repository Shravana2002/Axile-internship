// 1️⃣ Alert on Button Click
function showAlert() {
    alert("Button Clicked Successfully!");
}

// 2️⃣ Form Validation
document.getElementById("myForm").addEventListener("submit", function(event) {

    let name = document.getElementById("name").value;
    let email = document.getElementById("email").value;

    if (name === "" || email === "") {
        alert("All fields are required!");
        event.preventDefault();  // Stop form submission
    } else {
        alert("Form Submitted Successfully!");
    }
});

// 3️⃣ Simple Calculator
function calculate(operation) {

    let num1 = parseFloat(document.getElementById("num1").value);
    let num2 = parseFloat(document.getElementById("num2").value);
    let result;

    if (isNaN(num1) || isNaN(num2)) {
        alert("Please enter valid numbers!");
        return;
    }

    if (operation === "+") {
        result = num1 + num2;
    } 
    else if (operation === "-") {
        result = num1 - num2;
    } 
    else if (operation === "*") {
        result = num1 * num2;
    } 
    else if (operation === "/") {
        if (num2 === 0) {
            alert("Cannot divide by zero!");
            return;
        }
        result = num1 / num2;
    }

    document.getElementById("result").innerHTML = "Result: " + result;
}

// 4️⃣ Change Text on Click
function changeText() {
    document.getElementById("text").innerHTML = "Text Changed Successfully!";
}
