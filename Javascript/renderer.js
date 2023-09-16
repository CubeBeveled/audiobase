const { ipcRenderer } = require('electron');

// Close the window when the "Close" button is clicked
const closeButton = document.getElementById('close-btn');
closeButton.addEventListener('click', () => {
  ipcRenderer.send('close-window');
});
