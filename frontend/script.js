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
});