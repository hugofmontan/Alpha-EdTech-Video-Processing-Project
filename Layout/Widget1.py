from Tools import*
from PyQt6.QtGui import*
from PyQt6.QtCore import*
from PyQt6.QtWidgets import*
from PyQt6.QtCore import*
import cv2
import numpy as np


class VideoThread(QThread): #controle da entrada de video
    change_pixmap_signal = pyqtSignal(np.ndarray)

    def __init__(self):
        super().__init__()
        self._run_flag = True

    def run(self):
        cap = cv2.VideoCapture(0) #Entrada de video
        while self._run_flag:
            ret, cv_img = cap.read()
            if ret:
                self.change_pixmap_signal.emit(cv_img) #Envia o pixmap em Cv pro conversor pra Qt
        cap.release()

    def stop(self):
        self._run_flag = False
        self.wait()

class VideoThread2(QThread): #controle da entrada de video 2
    change_pixmap_signal = pyqtSignal(np.ndarray)

    def __init__(self):
        super().__init__()
        self._run_flag = True

    def run(self):
        cap = cv2.VideoCapture(1) #Entrada de video
        while self._run_flag:
            ret, cv_img = cap.read()
            if ret:
                self.change_pixmap_signal.emit(cv_img) #Envia o pixmap em Cv pro conversor pra Qt
        cap.release()

    def stop(self):
        self._run_flag = False
        self.wait()

class widget1():
    def Telinha1(self):
        widget1 = QWidget(self)
        widget1.setFixedSize(1280,720) #Tamanho fixo pra Tab1
        layout1 = QGridLayout()
        widget1.setLayout(layout1)
        layout1.addWidget(Color('darkgray'), 0, 0, 720, 1280) #corpo principal
        layout1.addWidget(Color('white'), 50, 50, 620, 1180)  #corpo secundário
        
        self.Cam1 = QLabel() #Camera 1
        self.Cam1.setObjectName('cam1')
        self.Cam1.setFixedSize(540, 400) #Tamanho fixo pro objeto "Cam1"
        self.Cam1.setStyleSheet('background-color: gray;')
        layout1.addWidget(self.Cam1, 250, 75, 400, 540)
        
        self.Cam2 = QLabel() #Camera 2
        self.Cam2.setObjectName('cam2')
        self.Cam2.setFixedSize(540, 400) #Tamanho fixo pro objeto "Cam2"
        self.Cam2.setStyleSheet('background-color: gray;')
        layout1.addWidget(self.Cam2, 250, 665, 400, 540)

        Not1 = QLabel() #Area de Notificação 1
        Not1.setObjectName('Notif1')
        Not1.setFixedSize(540, 70) #Tamanho fixo pro objeto "Notif1"
        Not1.setStyleSheet('background-color: green;')
        layout1.addWidget(Not1, 75, 75, 70, 540)

        Not2 = QLabel() #Area de Notificação 2
        Not2.setObjectName('Notif2')
        Not2.setFixedSize(540, 70) #Tamanho fixo pro objeto "Notif2"
        Not2.setStyleSheet('background-color: green;')
        layout1.addWidget(Not2, 75, 665, 70, 540)



        self.thread = VideoThread() #Video1
        self.thread.change_pixmap_signal.connect(self.update_image1) #Converte de CV pra Qt no Video1
        self.thread.start()

        self.thread2 = VideoThread2() #Video2
        self.thread2.change_pixmap_signal.connect(self.update_image2) #Converte de CV pra Qt no Video2
        self.thread2.start()
        
        return widget1