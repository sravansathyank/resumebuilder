 // JavaScript for input validation
 document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');
    form.addEventListener('submit', function (e) {
        const inputs = form.querySelectorAll('input, textarea, select');
        let valid = true;

        inputs.forEach(input => {
            if (!input.value.trim()) {
                input.style.borderColor = 'red';
                valid = false;
            } else {
                input.style.borderColor = '#ddd';
            }
        });

        if (!valid) {
            alert('Please fill in all the required fields.');
            e.preventDefault();
        }
    });
});