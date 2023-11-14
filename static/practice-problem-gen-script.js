// functions.js


let frames = []; // Global variable to store frames
const images = []; // Array to store the added images
const WIDTH = 384;
const HEIGHT = 288;
const TEMP = "static/practice_problem_gen_temp/";

// get all .bordered-div style and set width and height to WDITH and HEIGHT
const borderedDivs = document.querySelectorAll('.bordered-div');

// Loop through each element and set the CSS properties
borderedDivs.forEach((element) => {
  element.style.width = WIDTH + 'px';
  element.style.height = HEIGHT + 'px';
});

// Function to parse a GIF file
function recieveGif() {
  const fileInput = document.getElementById('fileInput');
  const file = fileInput.files[0];

  if (!file) {
      alert('Please select a GIF file.');
      return;
  }

  // Create a FormData object to send the file
  const formData = new FormData();
  formData.append('gif', file);

  // Send the GIF file to the backend using fetch
  fetch('/practice-problem-generator/parse-gif', {
      method: 'POST',
      body: formData
  })
  .then(response => response.json())
  .then(data => {
    // Handle the response data from the backend as needed
    console.log('Success:', data);

    // You can now work with the parsed frames stored in frames
    updateSelectedFrame();
  })
  .catch(error => {
      console.error('Error:', error);
  });
}

// Function to display a selected frame
function updateSelectedFrame(num) {
    console.log('updateSelectedFrame() called');

    const frameSlider = document.getElementById('frameSlider');
    const frameDisplay = document.getElementById('frameDisplay');
  
    // Get the value of the slider (frame index)
    const selectedFrameIndex = parseInt(frameSlider.value);

    // Create an image element to display the selected frame
    const img = document.createElement('img');

    // Construct the URL for the image using the base URL passed from Flask
    // load image path from static, don't allow  cached images
    const name = getFileName();

    const imgpath = TEMP + name + "-" + selectedFrameIndex + ".png";
    img.src = imgpath;
    img.width = WIDTH;
    img.height = HEIGHT;
    // Clear the frameDisplay element and append the new image
    frameDisplay.innerHTML = '';
    frameDisplay.appendChild(img);
    
  }

  function addFrame() {
    const frameSlider = document.getElementById('frameSlider');
    const selectedFrameIndex = parseInt(frameSlider.value);
    const name = getFileName();
    const imgpath = TEMP + name + "-" + selectedFrameIndex + ".png";
    const img = document.createElement('img');
    img.src = imgpath;

    // Get the existing image element from frameDisplay
    if (img) {
        // Take the existing image and add it to the images array
        images.push(img);

        // Draw all images onto the canvas
        drawImagesOnCanvas(1);
    }
}

// Function to draw all images from the images array onto the canvas
function drawImagesOnCanvas(number) {
  // create canvas and attach to cardDisplay
  const canvas = document.createElement('canvas');
  canvas.width = WIDTH;
  canvas.height = HEIGHT;
  const cardDisplay = document.getElementById('cardDisplay');
  cardDisplay.innerHTML = '';
  cardDisplay.appendChild(canvas);

  // Get the canvas context
  const ctx = canvas.getContext('2d');

  // Clear the canvas
  ctx.clearRect(0, 0, canvas.width, canvas.height);


  //Adjust every image to have a 4:3 aspect ratio
  const desiredImageWidth = WIDTH / images.length;
  const desiredAspectRatio = desiredImageWidth / HEIGHT;

  for (let i = 0; i < images.length; i++) {


    const image = images[i];
    

    const imageAspectRatio = image.width / image.height;
    const destinationX = i * desiredImageWidth;
    let croppingHeight, croppingOffsetY, croppingWidth, croppingOffsetX; // Declare the variables here
    if (imageAspectRatio >= desiredAspectRatio) { //Image is wider than desired aspect ratio
      
      //Calculate cropping area
      croppingHeight = image.height;
      croppingOffsetY = 0;
      croppingWidth = image.height * desiredAspectRatio;
      croppingOffsetX = (image.width - croppingWidth) / 2;
      
    } else { //Image is taller than desired aspect ratio
      //Calculate cropping area
      croppingWidth = image.width;
      croppingOffsetX = 0;
      croppingHeight = image.width / desiredAspectRatio;
      croppingOffsetY = (image.height - croppingHeight) / 2;
    }

    // // Add the image to the canvas with cropping
    ctx.drawImage(
      image,
      croppingOffsetX,
      croppingOffsetY,
      croppingWidth,
      croppingHeight,
      destinationX,
      0,
      desiredImageWidth,
      HEIGHT
    );


  }

  // Add text to the canvas
  const fontSize = 200;
  
  // Set the font style and size
  ctx.font = `bold ${fontSize}px Arial`;
  ctx.textAlign = 'center';
  ctx.textBaseline = 'middle';
  
  // Apply the smooth shadow effect to the text on the text canvas
  ctx.shadowColor = "rgba(0, 0, 0, .8)";
  ctx.shadowBlur = 15;
  ctx.shadowOffsetX = 0;
  ctx.shadowOffsetY = 0;
  
  ctx.fillStyle = 'white';
  ctx.strokeStyle = 'black';
  ctx.lineWidth = 1;
  
  ctx.fillText(number, WIDTH / 2, HEIGHT / 2);
  ctx.strokeText(number, WIDTH / 2, HEIGHT / 2);

}
  

function saveCard() {

  // Get int from number input
  const numberInput = document.getElementById('numberInput');
  const number = parseInt(numberInput.value);

  // for loop up to number
  for (let i = 1; i <= number; i++) {
    drawImagesOnCanvas(i);
    // Get the cardDisplay element
    const cardDisplay = document.getElementById('cardDisplay');
    // Get the canvas element from cardDisplay
    const canvas = cardDisplay.querySelector('canvas');
    // Convert the canvas to a data URL
    const dataURL = canvas.toDataURL();
    // Add filename to dataURL as the form name
    const filename = getFileName();
    const blob = dataURLtoBlob(dataURL);


    // Create a FormData object to send the data
    const formData = new FormData();
    
    formData.append('card', blob);

    // Get input called id="fileNameInput" 
    const fileNameInput = document.getElementById('fileNameInput');
    formData.append('filename',  fileNameInput.value + "-" + i);
    formData.append('projectname', fileNameInput.value + "-practice-problem-" + i)

    // Add value of id="mcqInput" to formData as num_mcqs
    const mcqInput = document.getElementById('mcqInput-'+i);
    formData.append('num_mcqs', mcqInput.value);

    

    // Send the data to the backend using fetch
    fetch('/save_card', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        // Handle the response data from the backend as needed
        console.log('Success:', data);
    })
    .catch(error => {
        console.error('Error:', error);
    });
  }

  // get request /open_save_dir
  fetch('/open_save_dir', {
    method: 'GET',
  })
}

function clearCard() {
  // Clear the images array
  images.length = 0;

  // Draw all images onto the canvas
  drawImagesOnCanvas(1);
}

function getFileName() {
  const fileInput = document.getElementById('fileInput');
  const name = fileInput.files[0].name;
  // remove extension
  return name.split('.')[0];
}

// Function to convert data URL to Blob
function dataURLtoBlob(dataURL, filename) {
  const arr = dataURL.split(',');
  const mime = arr[0].match(/:(.*?);/)[1];
  const bstr = atob(arr[1]);
  let n = bstr.length;
  const u8arr = new Uint8Array(n);

  while (n--) {
      u8arr[n] = bstr.charCodeAt(n);
  }

  return new Blob([u8arr], { type: mime, filename: filename });
}

function setMcqAmount(){
  // Get number of cards from number input
  const numberInput = document.getElementById('numberInput');
  const number = parseInt(numberInput.value);
  // Get the mcq input element
  const mcqContainer = document.getElementById('mcq-count-container');
  // Clear the mcqContainer
  mcqContainer.innerHTML = '';
  // for loop over number of cards
  for (let i = 1; i <= number; i++) {
    // create a div with class row
    const row = document.createElement('div');
    row.classList.add('row');
    // Add a column with p contaning i
    const p = document.createElement('p');
    p.innerHTML = '#'+i+"=";
    row.appendChild(p);
    // Add a column with input
    // Create a new number input element
    const mcqInput = document.createElement('input');
    mcqInput.type = 'number';
    mcqInput.id = 'mcqInput-'+i;
    mcqInput.value = 1;
    mcqInput.min = 1;
    mcqInput.max = 10;
    mcqInput.step = 1;
    // Append the mcqInput to row
    row.appendChild(mcqInput);
    // Append the new input element to the mcqContainer
    mcqContainer.appendChild(row);
  }
}

function ReplaceUUIDs(event) {
    var fileInput = document.getElementById('uuid-fileInput');
    var file = fileInput.files[0];
    // Create a FormData object to send the file
    var formData = new FormData();
    formData.append('file', file);
    // Send the file to the backend using fetch
    fetch('/replace_uuids', {
        method: 'POST',
        body: formData
    })
}


// Initializes the PP bulider section
clearCard();
setMcqAmount();