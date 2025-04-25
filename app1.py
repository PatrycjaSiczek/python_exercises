import sys

from PyQt5 import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    
    #konstruktor
    def __init__(self):
        super().__init__() 
        
        self.setWindowTitle("My APP!")
        self.button = QPushButton("My button")
        self.button.clicked.connect(self.button_was_clicked)
        self.setCentralWidget(self.button)
        
    def button_was_clicked(self):
        print("Clicked!")
        self.button.setText("CLicked!")
        self.button.setEnabled(False)
        
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()