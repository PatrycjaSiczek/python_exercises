import sys

from PyQt5 import Qt
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QVBoxLayout, QLabel, QLineEdit, QWidget)

class MainWindow(QMainWindow):
    
    #konstruktor
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Moja Aplikacja")
        self.central_widget = QWidget()
        
        self.layout = QVBoxLayout(self.central_widget)
        
        self.button = QPushButton("Przycisk")
        self.button.clicked.connect(self.nacisniety)
        self.layout.addWidget(self.button)
        
        self.label = QLabel("Etykieta")
        self.layout.addWidget(self.label)
        
        self.linia = QLineEdit("Wprowadz tekst:")
        self.layout.addWidget(self.linia)
        
        self.setCentralWidget(self.central_widget)

    def nacisniety(self):
        text = self.linia.text().upper()
        count = text.count("G") + text.count("C")
        self.label.setText(f"Zawartosc GC: {count/len(text)}")
        print(text)
        
        
        
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()