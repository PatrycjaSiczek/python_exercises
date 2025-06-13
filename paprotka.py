import sys
import numpy as np
import random
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QPushButton, QSpinBox, QLabel, QLineEdit, QGridLayout
)

import pyqtgraph as pg


class MainWindow(QMainWindow):
    
    def __init__(self):
        
        super().__init__()
        self.setWindowTitle("Paprotka")
        
        self.widget = QWidget()
        self.setCentralWidget(self.widget)
        self.wyjscie = QVBoxLayout(self.widget)
        layout = QGridLayout()
        self.wyjscie.addLayout(layout)
        
        layout.addWidget(QLabel("Transformacja"), 0, 0)
        
        for j, name in enumerate("abcdef"):
            layout.addWidget(QLabel(name), 0, j + 1)

        self.fields = []  

        for i in range(4):  
            layout.addWidget(QLabel(f"T{i+1}"), i + 1, 0)
            row = []
            for j in range(6):
                field = QLineEdit("0.0")  
                layout.addWidget(field, i + 1, j + 1)
                row.append(field)
            self.fields.append(row)


        self.iter_label = QLabel("Iteracje:")
        self.iter_spinbox = QSpinBox()
        self.iter_spinbox.setRange(1000, 50000)
        self.iter_spinbox.setValue(10000)
        layout.addWidget(self.iter_label, 5, 0)
        layout.addWidget(self.iter_spinbox, 5, 1)

      
        self.prawdopodobienstwo = QLabel("Prawdopodobieństwa (4):")
        self.pokazprawdopodobienstwo = QLineEdit("0.01,0.85,0.07,0.07")
        layout.addWidget(self.prawdopodobienstwo, 5, 0)
        layout.addWidget(self.pokazprawdopodobienstwo, 5, 2, 2, 5)

        self.przycisk = QPushButton("Start")
        self.przycisk.clicked.connect(self.animacja)
        self.wyjscie.addWidget(self.przycisk)

        self.widgety= pg.PlotWidget(title="Paprotka")
        self.data = self.widgety.plot([], [], pen=None, symbol="o", symbolSize=1, symbolBrush="g")
        self.wyjscie.addWidget(self.widgety)


    def paprotka(self):
        fun = []
        
        p = list(
                 map(
                     float, self.pokazprawdopodobienstwo.text().split(',')))

        for row in self.fields:
            a, b, c, d, e, f = [float(field.text()) for field in row]
            fun.append(
                lambda x, y, a=a, b=b, c=c, d=d, e=e, f=f:
                    (a * x + b * y + e, c * x + d * y + f))
        return fun, p
    
    def animacja(self):
    
        n = self.iter_spinbox.value()
        fun, p = self.paprotka()
        x, y = self.losowo(n, fun, p)
        self.data.setData(x, y)
        self.setWindowTitle(f"Paprotka")
    
    def losowo(self, n, fun, p):
        
        x = np.zeros(n)
        y = np.zeros(n)

        for i in range(1, n):
            f = random.choices(fun, weights=p)[0]
            x[i], y[i] = f(x[i - 1], y[i - 1])
        return x, y

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
