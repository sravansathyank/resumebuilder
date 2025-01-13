// register.js

const form = document.querySelector('form');
const usernameInput = document.getElementById('id_username');
const emailInput = document.getElementById('id_email');
const passwordInput = document.getElementById('id_password');
const confirmPasswordInput = document.getElementById('id_confirm_password');

form.addEventListener('submit', (event) => {
  event.preventDefault(); // Prevent default form submission

  // Basic validation (you can add more complex validation as needed)
  if (usernameInput.value.trim() === '') {
    alert('Please enter a username');
    return;
  }

  if (emailInput.value.trim() === '') {
    alert('Please enter an email address');
    return;
  }

  if (passwordInput.value.trim() === '') {
    alert('Please enter a password');
    return;
  }

  if (confirmPasswordInput.value !== passwordInput.value) {
    alert('Passwords do not match');
    return;
  }

  // If validation passes, submit the form
  form.submit();
});