function loadFile(event) {
    const fileInput = document.getElementById('fileInput');
    const file = fileInput.files[0];

    if (!file) {
        alert('Please select a GIF file.');
        return;
    }

    // Create a FormData object to send the file
    const formData = new FormData();
    formData.append('file', file);

    // Send the GIF file to the backend using fetch
    fetch('/uuid-replacer/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        // Handle the response data from the backend as needed
        console.log('Success:', data);
        alert("File was converted successfully. If the Output folder did not appear, navigate to your HWEditor repo, and look for an Output folder at the root level. Your file should be in there.");
    })
    .catch(error => {
        console.error('Error:', error);
        alert("Ut oh! An error occured. Please ensure that your json file is formatted correctly. You can use the linter included in our Make tools first. After that, if you are still having issues, please send me the file you are editing so I can try to reproduce the error. Thanks!")
    });
}