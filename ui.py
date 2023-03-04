from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QLineEdit, QListWidget
import connection

class Window(QMainWindow):
    def __init__(self, conec: connection.Connection) -> None:
        super(Window, self).__init__()
        self.conec = conec

        # Lista de mensagens
        self.msg_list = QListWidget(self)
        self.msg_list.move(20, 20)
        self.msg_list.resize(680, 330)

        # linha de envio
        title_label = QLabel("Escreva sua mensagem:", self)
        title_label.move(20, 360)
        title_label.resize(200, 30)

        self.send_line = QLineEdit(self)
        self.send_line.move(20, 400)
        self.send_line.resize(680, 120)

        # Botão enviar
        send_button = QPushButton("Enviar", self)
        send_button.move(620, 360)
        send_button.resize(80, 30)
        send_button.clicked.connect(self.send_button_clicked)

        self.setGeometry(50, 50, 720, 540)
        self.setWindowTitle("GUI Chat")
        self.show()

    def send_button_clicked(self):
        self.conec.enviar(self.send_line.text())
        self.send_line.setText("")

    def receive(self, msg):
        self.msg_list.addItem(msg)
