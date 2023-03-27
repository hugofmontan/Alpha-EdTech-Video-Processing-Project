from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from Tools import *
from Tabs.Widget1 import*
from Tabs.Widget2 import*
from Tabs.Widget3 import*

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Alpha's Sentinel")
        self.setGeometry(0,0,1280,720)
        tabs = QTabWidget(self)
        tabs.setMovable(True)
        

        Widget1 = widget1.Telinha1(self)
        Widget2 = widget2.Telinha2(self)
        Widget3 = widget3.Telinha3(self)

        tabs.addTab(Widget1, "Cameras")
        tabs.addTab(Widget2, "Cadastro")
        tabs.addTab(Widget3, "Histórico")
        tabs.setTabShape(QTabWidget.TabShape.Triangular)
                 
        self.setCentralWidget(tabs)

    def update_image1(self, cv_img):
        qt_img = self.convert_cv_qt(cv_img)
        self.labelbox.setPixmap(qt_img)

    def update_image2(self, cv_img):
        qt_img = self.convert_cv_qt(cv_img)
        self.Cam2.setPixmap(qt_img)

    
    def convert_cv_qt(self, cv_img):
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format.Format_RGB888)
        p = convert_to_Qt_format.scaled(550, 420, Qt.AspectRatioMode.KeepAspectRatio)
        return QPixmap.fromImage(p)