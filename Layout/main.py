import sys
from PyQt6.QtWidgets import QApplication
from Janelaprincipal import *

app = QApplication(sys.argv)

janela = MainWindow()
janela.show()

app.exec()