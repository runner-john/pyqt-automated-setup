
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
