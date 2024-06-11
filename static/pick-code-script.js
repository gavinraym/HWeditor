const inputTextPickcode = document.getElementById('input-text-pickcode');
const displayAreaPickcode = document.getElementById('display-area-pickcode');

document.addEventListener('DOMContentLoaded', function () {
    inputTextPickcode.addEventListener('input', function () {
        const inputLines = inputTextPickcode.value.split('\n');
        const formattedLines = inputLines.map(line => `"${line.replace(/\\/g, '\\\\').replace(/"/g, '\\"')}"`);
        const formattedOutput = `[${formattedLines.join(', ')}]`;

        displayAreaPickcode.value = formattedOutput;
    });
});