const codeInput = document.getElementById('code-input');
const filenameInput = document.getElementById('filename-input');
const languageSelect = document.getElementById('language-select');
const actionSelect = document.getElementById("actionSelect");
const codeOutput = document.getElementById('code-output-display');
const finalOutput = document.getElementById('code-output-final');


let highlightedCode = "";

// Function to replace leading whitespace with &nbsp;
function replaceLeadingWhitespaceWithNbsp(text) {
    // Split the text into lines
    const lines = text.split('\n');
  
    // Process each line and replace leading whitespace with &nbsp;
    const processedLines = lines.map(line => {
      const leadingWhitespace = line.match(/^\s*/)[0]; // Match leading whitespace
      const nbspReplacement = '&nbsp;'.repeat(leadingWhitespace.length); // Create &nbsp; replacements
      return line.replace(/^\s*/, nbspReplacement); // Replace leading whitespace
    });
  
    // Join the processed lines back into a single string
    return processedLines.join('\n');
  }

function updateHighlight() {

    let inputText = codeInput.value;
    // if language is css:
    if (languageSelect.value === 'css') {
        inputText = replaceLeadingWhitespaceWithNbsp(inputText);
    } 

    // combine the mark and strike arrays
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
        // Set the textContent of the output element to replace all children
        '<span class="err">`</span><span class="css-property">nbsp</span><span class="err">`</span>'
        const pattern = /<span class="([^"]*)">&amp;<\/span><span class="([^"]*)">nbsp<\/span><span class="([^"]*)">;<\/span>/g;

        // Replace matching spans with custom content
        const text = data.highlighted_code.replace(pattern, (match, class1, class2, class3) => {
        // Replace with desired content, keeping the captured class attributes
        return `New content for class1="${class1}" class2="${class2}" class3="${class3}"`;
        });
        codeOutput.innerHTML = text;
        displayFinalOutput(text);
    })
    .catch(error => {
        console.error('Error:', error);
    });

}

let isMouseDown = false;
const hoveredNodes = [];

// Function to handle mouse down
function handleMouseDown() {
    console.log('handleMouseDown')
    isMouseDown = true;
    hoveredNodes.length = 0; // Clear the array on mouse down
}

// Function to handle mouse move while mouse button is down
function handleMouseMove(event) {
    if (isMouseDown) {
        // Get the target element under the mouse pointer
        const targetElement = document.elementFromPoint(event.clientX, event.clientY);

        // Check if the target element is not in the array before adding it
        if (
            !hoveredNodes.includes(targetElement) &&
            codeOutput.contains(targetElement) &&
            // is not class snippet-row
            !targetElement.classList.contains('snippet-row') &&
            !targetElement.classList.contains('line-number') &&
            !targetElement.classList.contains('code') &&
            !targetElement.classList.contains('mark') &&
            !targetElement.classList.contains('del')
            ) {
            // Push the target element into the array
            hoveredNodes.push(targetElement);
            console.log('Added to array');
            console.log(targetElement);
        } else {
        }
    }
}

// Function to handle mouse up
function handleMouseUp() {
    const element = actionSelect.value;
    isMouseDown = false;
    
    // Iterate over the nodes in the array on mouse up
    hoveredNodes.forEach(node => {
        // Do something with each node
        console.log(node);
        const markElement = document.createElement(element);

        // Step 3: Replace the anchor node with the <mark> element
        const parentElement = node.parentElement;
        console.log(parentElement)
        parentElement.replaceChild(markElement, node);

        // Step 4: Add the anchor node as a child of the <mark> element
        markElement.appendChild(node);
    });

    // Get the outer HTML of the selected content and its ancestors
    const selectedHTML = codeOutput.innerHTML;

    // Replace </div><div> with nothing in the innerHTML
    let modifiedHTML = selectedHTML.replace(/<\/mark>(\s*)<mark>/g, (match, spaces) => spaces);
    modifiedHTML = modifiedHTML.replace(/<\/del>(\s*)<del>/g, (match, spaces) => spaces);
    
    // Set the modified HTML back to the node
    codeOutput.innerHTML = modifiedHTML;

    displayFinalOutput(modifiedHTML);


    // Set the inner HTML as the text content of finalOutput
    

}

function displayFinalOutput(str) {
    if (filenameInput.value) {
        const filenamehtml = "<div class='snippet-row'><span class='filename'>" + filenameInput.value+ "</span></div>";
        finalOutput.textContent =  filenamehtml + str;
    } else {
        finalOutput.textContent = str;
    }
}

function clearAll() {
    updateHighlight();
}

function copyToClipboard() {
    // make server call to /copy_to_clipboard
    const formData = new FormData();
    formData.append('clip', finalOutput.textContent);

    // Send the data to the backend using fetch
    fetch('/copy_to_clipboard', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .catch (error => {
        console.error('Error:', error);
    });
  
}



// Add event listeners
document.addEventListener('mousedown', handleMouseDown);
document.addEventListener('mousemove', handleMouseMove);
document.addEventListener('mouseup', handleMouseUp);



