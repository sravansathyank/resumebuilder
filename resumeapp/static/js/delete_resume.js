// Assuming you have a button with the ID "delete-button"
const deleteButton = document.getElementById('delete-button');

deleteButton.addEventListener('click', () => {
  if (confirm('Are you sure you want to delete this resume?')) {
    // Proceed with the deletion, e.g., submit the form
    document.getElementById('delete-form').submit();
  }
});