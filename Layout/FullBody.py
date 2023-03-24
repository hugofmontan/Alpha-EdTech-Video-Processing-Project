from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
import sys
   

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Alpha's Sentinel")
        self.setGeometry(0,0,1280,720)

        tabs = QTabWidget(self)
        tabs.setMovable(True)
        

        widget1 = QWidget(self)
        layout1 = QGridLayout()
        widget1.setLayout(layout1)
        layout1.addWidget(Color('darkgray'), 0,0, 700, 1100)
        layout1.addWidget(Color('gray'), 250, 10, 400, 530)
        layout1.addWidget(Color('gray'), 250, 555, 400, 530)
        layout1.addWidget(Color('green'), 100, 10, 100, 530)
        layout1.addWidget(Color('green'), 100,555, 100, 530)



        widget2 = QWidget(self)
        layout2 = QGridLayout()
        widget2.setLayout(layout2)
        layout2.addWidget(Color('darkgray'), 0, 0, 800, 1200)
        layout2.addWidget(Color('green'), 102, 100, 50, 1000)
        layout2.addWidget(Color('gray'), 188, 100, 200, 1000)
        layout2.addWidget(Color('gray'), 423, 100, 300, 1000)

            
        layout2.addWidget(Color('lightgray'), 450, 125, 150, 150)
        layout2.addWidget(Color('lightgray'), 450, 300, 150, 150)
        layout2.addWidget(Color('lightgray'), 450, 475, 150, 10)
        layout2.addWidget(Color('lightgray'), 450, 650, 150, 150)

        layout2.addWidget(Color('black'), 450, 825, 250, 250)



        widget3 = QWidget(self)
        layout3 = QGridLayout()
        widget3.setLayout(layout3)
        layout3.addWidget(Color('darkgray'), 0, 0, 800, 1200)
        layout3.addWidget(Color('green'), 100, 100, 50, 1000)
 
        layout3.addWidget(Color('white'), 200, 100, 500, 700)
        layout3.addWidget(Color('black'), 200, 850, 500, 250)

        tabs.addTab(widget1, "Cameras")
        tabs.addTab(widget2, "Cadastro")
        tabs.addTab(widget3, "Histórico")
        tabs.setTabShape(QTabWidget.TabShape.Triangular)
                 
        self.setCentralWidget(tabs)


class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)

app = QApplication(sys.argv)

janela = MainWindow()
janela.show()

app.exec()