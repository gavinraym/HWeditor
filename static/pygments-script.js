const codeInput = document.getElementById('code-input');
const languageSelect = document.getElementById('language-select');
const actionSelect = document.getElementById("actionSelect");
const codeOutput = document.getElementById('code-output-display');
const finalOutput = document.getElementById('code-output-final');
const markStarts = [];
const markEnds = [];
const strikeStarts = [];
const strikeEnds = [];

let highlightedCode = "";

function updateHighlight() {

    let inputText = codeInput.value;

    // combine the mark and strike arrays
    const breaks = markStarts.concat(strikeStarts).concat(markEnds).concat(strikeEnds);
    console.log(breaks);
    console.log(breaks.sort((a, b) => b - a));
    breaks.sort((a, b) => b - a).forEach((index) => {
        console.log(index);
        console.log(markStarts);
        // Inside this function, 'index' will represent each value in the sorted array
        if (markStarts.includes(index)) {
            inputText = inputText.slice(0, index) + '`<mark>`' + inputText.slice(index);
        } else if (strikeStarts.includes(index)) {
            inputText = inputText.slice(0, index) + '`<del>`' + inputText.slice(index);
        } else if (markEnds.includes(index)) {
            inputText = inputText.slice(0, index) + '`</mark>`' + inputText.slice(index);
        } else if (strikeEnds.includes(index)) {
            inputText = inputText.slice(0, index) + '`</del>`' + inputText.slice(index);
        }
      });
    console.log(inputText);
    const formData = new FormData();
    formData.append('code', inputText);
    formData.append('language', languageSelect.value);

    // Send the data to the backend using fetch
    fetch('/highlight', {
        method: 'POST',
        body: formData
    })
    
    .then(response => response.json())
    .then(data => {
        // Handle the response data from the backend as needed
        console.log('Success:', data);
        // Set the textContent of the output element to replace all children
        codeOutput.innerHTML = data.highlighted_code;
        finalOutput.textContent = data.highlighted_code;
    })
    .catch(error => {
        console.error('Error:', error);
    });

}


codeInput.addEventListener('mouseup', () => {

    const selection = window.getSelection();
    const selectedText = selection.toString();

    if (selectedText) {

        // Find the start and end indices of the selected lines
        let startIndex = codeInput.selectionStart;

        let endIndex = codeInput.selectionEnd;

        // Add to mark or strike
        if (actionSelect.value == "mark") {
            markStarts.push(startIndex);
            markEnds.push(endIndex);
        } else if (actionSelect.value == "del") {
            strikeStarts.push(startIndex);
            strikeEnds.push(endIndex);
        } else if (actionSelect.value == "clear") {
            // remove all numbers between start and end from the mark and strike arrays
            for (let i = startIndex; i < endIndex+1; i++) {
                if (markStarts.includes(i)) {
                    markStarts.splice(markStarts.indexOf(i), 1);
                } else if (strikeStarts.includes(i)) {
                    strikeStarts.splice(strikeStarts.indexOf(i), 1);
                } else if (markEnds.includes(i)) {
                    markEnds.splice(markEnds.indexOf(i), 1);
                } else if (strikeEnds.includes(i)) {
                    strikeEnds.splice(strikeEnds.indexOf(i), 1);
                }
            }
        }
        updateHighlight();
    }
})

function clearAll() {
    markStarts.length = 0;
    markEnds.length = 0;
    strikeStarts.length = 0;
    strikeEnds.length = 0;
    updateHighlight();
}

function copyToClipboard() {

  console.log('copyToClipboard');
}