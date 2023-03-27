from Tools import*
from PyQt6.QtGui import*
from PyQt6.QtCore import*
from PyQt6.QtWidgets import*

class widget3():
    def Telinha3(self):
        widget3 = QWidget(self)
        widget3.setFixedSize(1280,720)
        layout3 = QGridLayout()
        widget3.setLayout(layout3)

        #Caixas de preenchimento
        #Criando e setando os parâmetros do background da plataforma
        corpo3 = QLabel()
        corpo3.setObjectName('corpo')
        corpo3.setFixedSize(1280, 720)
        corpo3.setStyleSheet('background-color: darkgray;')
        layout3.addWidget(corpo3, 0, 0, 720, 1280)

        #Caixas de preenchimento
        #Criando e setando os parâmetros da caixa branca de área útil
        caixa1 = QLabel()
        caixa1.setObjectName('caixa1')
        caixa1.setFixedSize(1180,620)
        caixa1.setStyleSheet('background-color: white;')
        layout3.addWidget(caixa1, 45, 53.33, 620, 1180)

        #Caixas de preenchimento
        #Criando e setando os parâmetros do background da caixa de notificação
        caixa2 = QLabel()
        caixa2.setObjectName('caixa2')
        caixa2.setFixedSize(1060, 45)
        caixa2.setStyleSheet('background-color: green;')
        layout3.addWidget(caixa2, 90, 100, 45, 1060)
  
        #Caixas de preenchimento
        #Criando e setando os parâmetros da caixa da planilha
        caixa3 = QLabel()
        caixa3.setObjectName('caixa3')
        caixa3.setFixedSize(745,450)
        caixa3.setStyleSheet('background-color: gray;')
        layout3.addWidget(caixa3, 180, 105, 450, 745)
 
        #Caixas de preenchimento
        #Criando e setando os parâmetros da caixa da planilha filtrada
        caixa4 = QLabel()
        caixa4.setObjectName('caixa4')
        caixa4.setFixedSize(255, 450)
        caixa4.setStyleSheet('background-color: black;')
        layout3.addWidget(caixa4, 180, 905, 450, 255)

        return widget3