import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QWidget, QSlider)

class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Moja Aplikacja")
        self.central_widget = QWidget()

        self.main_layout = QVBoxLayout(self.central_widget)
        self.top_layout = QHBoxLayout()
        self.bottom_layout = QHBoxLayout()
        
        self.label1 = QLabel("Suwak")
        self.top_layout.addWidget(self.label1)
        
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0,100)
        self.slider.setValue(50)
        self.slider.valueChanged.connect(self.update_label)
        self.top_layout.addWidget(self.slider)
        
        self.label2 = QLabel("50")
        self.top_layout.addWidget(self.label2)
        
        self.main_layout.addLayout(self.top_layout)
        self.bottom_layout.addLayout(self.bottom_layout)
        self.setCentralWidget(self.central_widget)
    
    def update_label(self, value):   
        self.label2.setText(str(value))
        
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()