// Assuming you have a class for delete links (e.g., .delete-resume)
const deleteLinks = document.querySelectorAll('.delete-resume');

deleteLinks.forEach(link => {
  link.addEventListener('click', (event) => {
    event.preventDefault(); // Prevent default link behavior

    if (confirm('Are you sure you want to delete this resume?')) {
      // Proceed with deletion (redirect to the delete URL)
      window.location.href = link.href;
    }
  });
});