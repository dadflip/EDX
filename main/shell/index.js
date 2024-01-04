const { app, BrowserWindow, ipcMain } = require('electron');
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

  mainWindow.loadFile('index.html');
  mainWindow.on('closed', function () {
    mainWindow = null;
  });

  const terminalDiv = mainWindow.webContents.executeJavaScript("document.getElementById('terminal')");

  const terminal = spawn('bash');

  terminal.stdout.on('data', (data) => {
    mainWindow.webContents.send('terminal-data', data.toString());
  });

  ipcMain.on('user-input', (event, input) => {
    terminal.stdin.write(input + '\n');
  });
}

app.on('ready', createWindow);

app.on('window-all-closed', function () {
  if (process.platform !== 'darwin') app.quit();
});

app.on('activate', function () {
  if (mainWindow === null) createWindow();
});

