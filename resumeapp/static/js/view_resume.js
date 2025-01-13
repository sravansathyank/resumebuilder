// resumeapp/static/js/view_resume.js

// Smooth scroll to the top of the page when clicking the "Back to Home" button
document.addEventListener("DOMContentLoaded", () => {
    const backButton = document.querySelector('.back-btn');
    backButton.addEventListener('click', (event) => {
        event.preventDefault();
        window.scrollTo({ top: 0, behavior: 'smooth' });
        setTimeout(() => {
            window.location.href = backButton.getAttribute('href');
        }, 600);
    });
});
