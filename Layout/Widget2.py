from Tools import*
from PyQt6.QtGui import*
from PyQt6.QtCore import*
from PyQt6.QtWidgets import*

class widget2():
    def Telinha2(self):
        #Definindo a criação do Widget na classe Grid
        widget2 = QWidget(self)
        layout2 = QGridLayout()

        widget2.setLayout(layout2)
        widget2.setFixedSize(1280,720)

        #Caixas de preenchimento
        #Criando e setando os parâmetros do backgroud da plataforma
        corpo2 = QLabel()
        corpo2.setObjectName('corpo')
        corpo2.setFixedSize(1280, 720)
        corpo2.setStyleSheet('background-color: darkgray;')
        layout2.addWidget(corpo2, 0, 0, 720, 1280)

        #Caixas de preenchimento
        #Criando e setando paramêtros da caixa de notificação
        notificacao = QLabel()
        notificacao.setObjectName('notificação')
        notificacao.setFixedSize(1000, 80)
        notificacao.setStyleSheet('background-color: green;')
        layout2.addWidget(notificacao, 70, 140, 80, 1000)

        #Caixas de preenchimento
        #Criando e setando parâmetros da caixa dos dados inputados
        dados = QLabel()
        dados.setObjectName('texto')
        dados.setFixedSize(200, 450)
        dados.setStyleSheet('background-color: gray;')
        layout2.addWidget(dados, 172, 113, 450, 200)
        
        #Caixas de preenchimento
        #Criando e setando parâmetros das caixas de imagens/qrcode
        imagens = QLabel()
        imagens.setObjectName('imgs')
        imagens.setFixedSize(750, 450)
        imagens.setStyleSheet('background-color: gray;')
        layout2.addWidget(imagens, 172, 423, 450, 750)


        #Título de caixa
        #Criando título da caixa de informações pessoais
        texto1 = QLabel('Informações pessoais:')
        texto1.setFixedWidth(200)
        font = QFont('Bahnschrift', 11)
        texto1.setFont(font)
        layout2.addWidget(texto1, 200, 138, 20, 150)

        #Caixa do QR Code
        #Criando o dimensionamento do QR Code exibido
        qrcode = QLabel()
        qrcode.setObjectName('qrcode')
        qrcode.setFixedSize(250, 250)
        qrcode.setStyleSheet('background-color: black;')
        layout2.addWidget(qrcode, 272, 868, 250, 250)



        #Input de dados
        #Criando caixa de input do nome completo
        name = QLineEdit()
        name.setValidator(None)
        name.setMaxLength(40)
        name.setFont(QFont("Bahnschrift",10))
        name.setPlaceholderText('Nome completo:') #preview dos dados que devem ser inputados
        layout2.addWidget(name, 248, 138, 25, 150)

        #Input de dados
        #Criando caixa de input do CPF
        cpf = QLineEdit()
        cpf.setValidator(None)
        cpf.setMaxLength(40)
        cpf.setFont(QFont("Bahnschrift",10))
        cpf.setPlaceholderText('CPF:') #preview dos dados que devem ser inputados
        layout2.addWidget(cpf, 310, 138, 25, 150)

        #Input de dados
        #Criando caixa de input da data de nascimento
        data = QLineEdit()
        data.setValidator(None)
        data.setMaxLength(40)
        data.setFont(QFont("Bahnschrift",10))
        data.setPlaceholderText('Data de nascimento:') #preview dos dados que devem ser inputados
        layout2.addWidget(data, 372, 138, 25, 150)


        #Input de imagens
        #Criando a caixa de input da imagem 1 (Frente de rosto)
        img1 = QLabel()
        img1.setObjectName('Frente')
        img1.setFixedSize(150, 150)
        img1.setStyleSheet('background-color: lightgray;')
        layout2.addWidget(img1, 219, 480, 150, 150)

        #Funcionalizando o botão de input da imagem 1
        lb1 = QLabel(widget2)
        button1 = QPushButton('Frente:', widget2)
        button1.move(505,290)
        button1.setFixedSize(108,24)
        l1 = QVBoxLayout()
        l1.addWidget(lb1)
        l1.addWidget(button1)

        def selecionar_imagem1():
            file_name, _ = QFileDialog.getOpenFileName(None, 'Frente:', '', 'Imagens (*.png *.xpm *.jpg *.bmp)')
            if file_name:
                pixmap = QPixmap(file_name)
                lb1.setScaledContents(True)
                lb1.setPixmap(pixmap)
                lb1.setGeometry(486,225,150,150)
                button1.hide()  # oculta o botão após a seleção da imagem

        button1.clicked.connect(selecionar_imagem1)


        #Input de imagens
        #Criando a caixa de input da imagem 2 (lado direto)
        img2 = QLabel()
        img2.setObjectName('Direito')
        img2.setFixedSize(150, 150)
        img2.setStyleSheet('background-color: lightgray;')
        layout2.addWidget(img2, 219, 674, 150, 150)
       
        #Funcionalizando o botão de input da imagem 2
        lb2 = QLabel(widget2)
        button2 = QPushButton('Lado direito:', widget2)
        button2.move(699,290)
        button2.setFixedSize(108,24)
        l2 = QVBoxLayout()
        l2.addWidget(lb2)
        l2.addWidget(button2)

        def selecionar_imagem2():
            file_name, _ = QFileDialog.getOpenFileName(None, 'Lado direito:', '', 'Imagens (*.png *.xpm *.jpg *.bmp)')
            if file_name:
                pixmap = QPixmap(file_name)
                lb2.setScaledContents(True)
                lb2.setPixmap(pixmap)
                lb2.setGeometry(679,225,150,150)
                button2.hide()  # oculta o botão após a seleção da imagem

        button2.clicked.connect(selecionar_imagem2)


        #Input de imagens
        #Criando a caixa de input da imagem 3 (lado esquerdo)
        img3 = QLabel()
        img3.setObjectName('esquerda')
        img3.setFixedSize(150, 150)
        img3.setStyleSheet('background-color: lightgray;')
        layout2.addWidget(img3, 411, 480, 150, 150)

        #Funcionalizando o botão de input da imagem 3

        lb3 = QLabel(widget2)
        button3 = QPushButton('Lado esquerdo:', widget2)
        button3.move(505,495)
        button3.setFixedSize(108,24)
        l3 = QVBoxLayout()
        l3.addWidget(lb3)
        l3.addWidget(button3)

        def selecionar_imagem3():
            file_name, _ = QFileDialog.getOpenFileName(None, 'Lado esquerdo:', '', 'Imagens (*.png *.xpm *.jpg *.bmp)')
            if file_name:
                pixmap = QPixmap(file_name)
                lb3.setPixmap(pixmap)
                lb3.setScaledContents(True)
                lb3.setGeometry(486,434,150,150)
                button3.hide()  # oculta o botão após a seleção da imagem

        button3.clicked.connect(selecionar_imagem3)


        #Input de imagens
        #Criando a caixa de input da imagem 4 (adicional)
        img4 = QLabel()
        img4.setObjectName('adicional1')
        img4.setFixedSize(150, 150)
        img4.setStyleSheet('background-color: lightgray;')
        layout2.addWidget(img4, 411, 674, 150, 150)

        ##Funcionalizando o botão de input da imagem 4
        lb4 = QLabel(widget2)
        button4 = QPushButton('Foto adicional:', widget2)
        button4.move(699,495)
        button4.setFixedSize(108,24)
        l4 = QVBoxLayout()
        l4.addWidget(lb4)
        l4.addWidget(button4)

        def selecionar_imagem4():
            file_name, _ = QFileDialog.getOpenFileName(None, 'Foto adicional:', '', 'Imagens (*.png *.xpm *.jpg *.bmp)')
            if file_name:
                pixmap = QPixmap(file_name)
                lb4.setPixmap(pixmap)
                lb4.setScaledContents(True)
                lb4.setGeometry(679,434,150,150)
                button4.hide()  # oculta o botão após a seleção da imagem

        button4.clicked.connect(selecionar_imagem4)



        #Configurações finais
        layout_principal = QVBoxLayout(widget2)
        layout_principal.addLayout(l1)
        layout_principal.addLayout(l2)
        layout_principal.addLayout(l3)
        layout_principal.addLayout(l4)
        widget2.setLayout(layout_principal)

    
        return widget2