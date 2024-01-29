document.addEventListener('DOMContentLoaded', function () {
    const fileInput = document.getElementById('fileInput');
    const fileInfo = document.getElementById('fileInfo');
    const drop = document.getElementById('dropzone');

    fileInput.addEventListener('change', function () {
        const fileName = fileInput.files[0].name;
        document.getElementById('fileName').textContent = fileName;

        // Show the file info
        fileInfo.style.display = 'block';
        drop.style.display = 'none';
    });
});