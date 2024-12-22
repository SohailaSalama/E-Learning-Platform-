document.addEventListener('DOMContentLoaded', function () {
    const fileInput = document.getElementById('file-input');
    const dragAreaLabel = document.querySelector('.drag-area-label');

    dragAreaLabel.addEventListener('click', function() {
        fileInput.click();
    });

    fileInput.addEventListener('change', function(event) {
        const fileName = event.target.files[0] ? event.target.files[0].name : 'No file selected';
        dragAreaLabel.textContent = `Selected file: ${fileName}`;
    });

    const form = document.getElementById('reset-password-form');
    const messagesDiv = document.getElementById('messages');

    form.addEventListener('submit', function (event) {
        event.preventDefault();

        const password = document.getElementById('password').value;
        const confirmPassword = document.getElementById('confirm_password').value;

        if (password !== confirmPassword) {
            messagesDiv.innerHTML = '<center><h4 style="color: firebrick;">Passwords do not match</h4></center>';
            return;
        }

        messagesDiv.innerHTML = '<center><h4 style="color: dodgerblue;">Password reset successful</h4></center>';
    });