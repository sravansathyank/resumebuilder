 // JavaScript to handle form validation
 document.querySelector('form').addEventListener('submit', function(event) {
    var username = document.querySelector('input[name="username"]').value;
    var password = document.querySelector('input[name="password"]').value;

    if (username === "" || password === "") {
        alert("Please fill in all fields.");
        event.preventDefault(); // Prevent form submission
    }
});