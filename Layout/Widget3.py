from Tools import*
from PyQt6.QtGui import*
from PyQt6.QtCore import*
from PyQt6.QtWidgets import*

class widget3():
    def Telinha3(self):
        widget3 = QWidget(self)
        layout3 = QGridLayout()
        widget3.setLayout(layout3)
        layout3.addWidget(Color('darkgray'), 0, 0, 800, 1200)
        layout3.addWidget(Color('green'), 100, 100, 50, 1000)
 
        layout3.addWidget(Color('white'), 200, 100, 500, 700)
        layout3.addWidget(Color('black'), 200, 850, 500, 250)
        return widget3