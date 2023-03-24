from Tools import*
from PyQt6.QtGui import*
from PyQt6.QtCore import*
from PyQt6.QtWidgets import*
from PyQt6.QtCore import*
import cv2
import numpy as np


class VideoThread(QThread):
    change_pixmap_signal = pyqtSignal(np.ndarray)

    def __init__(self):
        super().__init__()
        self._run_flag = True

    def run(self):
        cap = cv2.VideoCapture(0)
        while self._run_flag:
            ret, cv_img = cap.read()
            if ret:
                self.change_pixmap_signal.emit(cv_img)
        cap.release()

    def stop(self):
        self._run_flag = False
        self.wait()

class VideoThread2(QThread):
    change_pixmap_signal = pyqtSignal(np.ndarray)

    def __init__(self):
        super().__init__()
        self._run_flag = True

    def run(self):
        cap = cv2.VideoCapture(1)
        while self._run_flag:
            ret, cv_img = cap.read()
            if ret:
                self.change_pixmap_signal.emit(cv_img)
        cap.release()

    def stop(self):
        self._run_flag = False
        self.wait()

class widget1():
    def Telinha1(self):
        widget1 = QWidget(self)
        widget1.setFixedSize(1280,720)
        layout1 = QGridLayout()
        widget1.setLayout(layout1)
        layout1.addWidget(Color('darkgray'), 0, 0, 720, 1280)
        layout1.addWidget(Color('white'), 50, 50, 620, 1180)
        
        self.labelbox = QLabel()
        self.labelbox.setObjectName('cam1')
        self.labelbox.setFixedSize(540, 400)
        self.labelbox.setStyleSheet('background-color: gray;')
        layout1.addWidget(self.labelbox, 250, 75, 400, 540)
        
        self.Cam2 = QLabel()
        self.Cam2.setObjectName('cam2')
        self.Cam2.setFixedSize(540, 400)
        self.Cam2.setStyleSheet('background-color: gray;')
        layout1.addWidget(self.Cam2, 250, 665, 400, 540)

        Not1 = QLabel()
        Not1.setObjectName('cam2')
        Not1.setFixedSize(540, 70)
        Not1.setStyleSheet('background-color: green;')
        layout1.addWidget(Not1, 75, 75, 70, 540)

        Not2 = QLabel()
        Not2.setObjectName('cam2')
        Not2.setFixedSize(540, 70)
        Not2.setStyleSheet('background-color: green;')
        layout1.addWidget(Not2, 75, 665, 70, 540)



        self.thread = VideoThread()
        self.thread.change_pixmap_signal.connect(self.update_image1)
        self.thread.start()

        self.thread2 = VideoThread2()
        self.thread2.change_pixmap_signal.connect(self.update_image2)
        self.thread2.start()
        return widget1
    
    