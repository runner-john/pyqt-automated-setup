#!/usr/bin/env python3
"""
PyQt Automated Setup and Packaging Script
This script automates the installation of PyQt and PyInstaller,
creates a sample PyQt application, and packages it into a standalone executable.
"""

import sys
import subprocess
import shutil
from pathlib import Path


def run_command(cmd, description=""):
    """Run a shell command with error handling"""
    if description:
        print(f"{description}...")
    
    try:
        result = subprocess.run(
            cmd,
            shell=False,
            check=True,
            capture_output=True,
            text=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
        print(f"Command output: {e.stdout}")
        print(f"Command error: {e.stderr}")
        return None


def check_python_version():
    """Check if Python version is compatible"""
    version = sys.version_info
    print(f"Python Version: {version.major}.{version.minor}.{version.micro}")
    
    if version.major < 3 or (version.major == 3 and version.minor < 7):
        print("Warning: Python 3.7+ recommended for PyQt6")


def update_pip():
    """Update pip to the latest version"""
    run_command(
        [sys.executable, "-m", "pip", "install", "--upgrade", "pip"],
        "Updating pip"
    )


def install_dependencies():
    """Install required dependencies"""
    dependencies = [
        "PyQt6",
        "pyinstaller"
    ]
    
    for dep in dependencies:
        run_command(
            [sys.executable, "-m", "pip", "install", dep],
            f"Installing {dep}"
        )


def create_sample_application():
    """Create a simple PyQt6 application"""
    app_code = '''
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QVBoxLayout,
    QWidget,
    QPushButton
)


class PyQtDemoApp(QMainWindow):
    """Sample PyQt6 Application"""
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        """Initialize the user interface"""
        self.setWindowTitle("PyQt6 Automation Demo")
        self.setGeometry(100, 100, 450, 300)
        
        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout(central_widget)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Add title label
        title_label = QLabel("PyQt6 Automated Setup Complete!")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(title_label)
        
        # Add description label
        desc_label = QLabel("This application was created and packaged automatically.")
        desc_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(desc_label)
        
        # Add exit button
        exit_button = QPushButton("Exit")
        exit_button.clicked.connect(self.close)
        exit_button.setFixedWidth(100)
        layout.addWidget(exit_button, alignment=Qt.AlignmentFlag.AlignCenter)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PyQtDemoApp()
    window.show()
    sys.exit(app.exec())
'''
    
    with open("pyqt_demo_app.py", "w", encoding="utf-8") as f:
        f.write(app_code)
    
    print("Created sample application: pyqt_demo_app.py")


def create_requirements_file():
    """Create a requirements.txt file"""
    requirements = """
PyQt6
pyinstaller
"""
    
    with open("requirements.txt", "w") as f:
        f.write(requirements.lstrip())
    
    print("Created requirements.txt file")


def package_application():
    """Package the application using PyInstaller"""
    # Clean previous builds if they exist
    for dir_path in ["build", "dist"]:
        if Path(dir_path).exists():
            try:
                shutil.rmtree(dir_path)
                print(f"Cleaned previous {dir_path} directory")
            except PermissionError:
                print(f"Warning: Cannot clean {dir_path} directory (permission denied). Continuing...")
            except Exception as e:
                print(f"Warning: Error cleaning {dir_path} directory: {e}. Continuing...")
    
    # Run PyInstaller to create a single executable
    result = run_command(
        [sys.executable, "-m", "PyInstaller", 
         "--onefile", "--windowed", 
         "--name", "PyQtDemo", 
         "pyqt_demo_app.py"],
        "Packaging application with PyInstaller"
    )
    
    if result is not None:
        print("Packaging completed successfully!")
        print("Executable location: dist/PyQtDemo.exe")
    else:
        print("Packaging might have failed. Check the output above.")


def main():
    """Main function to run the setup process"""
    print("=" * 50)
    print("PYQT AUTOMATED SETUP AND PACKAGING SCRIPT")
    print("=" * 50)
    
    # Step 1: Check Python version
    check_python_version()
    
    # Step 2: Update pip
    update_pip()
    
    # Step 3: Install dependencies
    install_dependencies()
    
    # Step 4: Create sample application
    create_sample_application()
    
    # Step 5: Create requirements file
    create_requirements_file()
    
    # Step 6: Package the application
    package_application()
    
    print("\n" + "=" * 50)
    print("SETUP COMPLETE!")
    print("=" * 50)


if __name__ == "__main__":
    main()
