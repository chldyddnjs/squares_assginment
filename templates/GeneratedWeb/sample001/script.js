document.getElementById("login-form").addEventListener("submit", function(event){
    event.preventDefault(); // prevent form submission

    // Perform login verification here
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;

    // Example login validation - check if email and password match
    if (email === "user@example.com" && password === "password") {
        alert("Login successful!");
        // Redirect to another page or perform any other action after successful login
    } else {
        alert("Invalid email or password. Please try again.");
        // Clear the form inputs for incorrect credentials
        document.getElementById("email").value = "";
        document.getElementById("password").value = "";
    }
});
