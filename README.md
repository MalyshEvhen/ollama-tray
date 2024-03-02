# Tray App 🖥️

## Table of Contents
- [Features](#features)
- [Usage](#usage) 
- [Building](#building)
- [Systemd Service](#systemd-service)
- [Icon](#icon)

This is a simple desktop app that runs in the system tray.

## Features 🚀

- Shows an icon in the system tray
- Provides a context menu with options when clicked:
  - Run ollama list command
  - Quit app
- Shows output of ollama list command in a pop-up message box
- Shows error message if ollama list fails

## Usage 💻

To run the app:

```
python tray_app.py
```

This will launch the app which will show up in the system tray. 

To quit the app, right click on the tray icon and click "Quit".

## Building 🛠️

The app can be packaged into a standalone executable using PyInstaller:

```  
pyinstaller tray_app.spec
```

This will generate a dist/tray_app executable that can be run on any system with the same OS and architecture.

The PyInstaller spec file includes the app icon in the assets folder.

## Systemd Service 🚦

To create a systemd service to run the tray app at startup:

1. Create a service file e.g. /etc/systemd/system/tray_app.service  
2. Add the following:
    ```
    [Unit]
    Description=Tray App

    [Service]  
    ExecStart=/path/to/tray_app
    WorkingDirectory=/path/to/tray_app/folder

    [Install]
    WantedBy=multi-user.target
    ```
3. Run `sudo systemctl enable tray_app` to enable the service
4. Start it with `sudo systemctl start tray_app`

Now the tray app will run automatically on system startup. 

## Icon 🖼️

The ollama icon is used from IconArchive under CC BY 3.0 license.
