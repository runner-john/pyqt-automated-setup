# PyQt Automated Setup and Packaging

This repository contains a Python script that automates the installation of PyQt6 and PyInstaller, creates a sample PyQt6 application, and packages it into a standalone executable.

## Files Included

- `pyqt_automated_setup.py` - Main automation script that handles installation and packaging
- `pyqt_demo_app.py` - Sample PyQt6 GUI application
- `requirements.txt` - List of required dependencies
- `dist/PyQtDemo.exe` - Standalone executable (generated after running the script)
- `README.md` - This documentation file

## Prerequisites

- Python 3.7 or higher
- Windows operating system (for .exe generation)

## How to Use

### 1. Run the Automated Setup Script

Execute the main script to perform the entire process automatically:

```bash
python pyqt_automated_setup.py
```

This will:
- Check your Python version
- Update pip to the latest version
- Install PyQt6 and PyInstaller
- Create the sample application
- Generate a requirements.txt file
- Package the application into a standalone executable

### 2. Install Dependencies Only

If you only want to install the required dependencies:

```bash
python -m pip install -r requirements.txt
```

### 3. Run the Sample Application

To run the sample application without packaging:

```bash
python pyqt_demo_app.py
```

### 4. Package the Application Manually

To package the application manually:

```bash
python -m PyInstaller --onefile --windowed --name PyQtDemo pyqt_demo_app.py
```

## Running the Packaged Executable

After successful packaging, you can find the executable at `dist/PyQtDemo.exe`.

- Double-click `PyQtDemo.exe` to launch the application
- Or run it from the command line:
  ```bash
dist\PyQtDemo.exe
  ```

The executable is self-contained and doesn't require Python or PyQt to be installed on other machines.

## Sample Application Features

The generated sample application includes:
- A simple window with a title
- A centered title label
- A description label
- An exit button