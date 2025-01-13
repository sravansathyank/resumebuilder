// update_resume.js

const form = document.querySelector('form');
const requiredFields = document.querySelectorAll('.required');

form.addEventListener('submit', (event) => {
  event.preventDefault(); // Prevent default form submission

  let isValid = true;

  requiredFields.forEach(field => {
    if (field.value.trim() === '') {
      alert('Please fill in all required fields');
      isValid = false;
    }
  });

  if (isValid) {
    form.submit();
  }
});