function Update() {
    // get <select id="content-type"> value and check if it is first or second option
    var contentType = document.getElementById("content-type").value;
    // create url for ajax request
    var url = "/multiple-choice-generator/" + contentType;
    // Get number of questions from <input id="number-of-questions">
    var numberOfQuestions = document.getElementById("number-of-questions").value;

    // Create a FormData object to send the file
    const formData = new FormData();
    formData.append('number-of-questions', numberOfQuestions);

    fetch(url, {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        // Add returned data to textarea class="json-editor"
        document.getElementById("json-editor").value = JSON.stringify(data, null, 4);
    })
    .catch(error => {
        console.error('Error:', error);
    });

}


function saveToClipboard() {
    // Get the text field
    var copyText = document.getElementById("json-editor");

    // Select the text field
    copyText.select();

    // Copy the text inside the text field
    navigator.clipboard.writeText(copyText.value);

}

function refresh() {
    Update();
}

function openFile() {
    // get request /open_save_dir
    fetch('/open_save_dir', {
        method: 'GET',
    })
}

refresh();
