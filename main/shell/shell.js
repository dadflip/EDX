const { app, BrowserWindow } = require('electron');
const { spawn } = require('child_process');
let mainWindow;

function createWindow() {
  mainWindow = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      nodeIntegration: true,
    },
  });

  mainWindow.loadFile('src/index.html');
  mainWindow.on('closed', function () {
    mainWindow = null;
  });

  const terminalDiv = mainWindow.webContents.executeJavaScript("document.getElementById('terminal')");

  const terminal = spawn('bash'); // Vous pouvez utiliser un autre shell si nécessaire

  terminal.stdout.on('data', (data) => {
    terminalDiv.then((element) => {
      element.innerHTML += data.toString();
    });
  });

  mainWindow.webContents.on('before-input-event', (event, input) => {
    if (input.type === 'keyDown') {
      if (input.key === 'Enter') {
        terminal.stdin.write('\n');
      } else {
        terminal.stdin.write(input.key);
      }
    }
  });
}

app.on('ready', createWindow);

app.on('window-all-closed', function () {
  if (process.platform !== 'darwin') app.quit();
});

app.on('activate', function () {
  if (mainWindow === null) createWindow();
});

