import socket
from threading import Thread

host = input("Digite o IP do servidor: ")
port = 2000

clie = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET = IPV4 | SOCK_STREAM = TCP
clie.connect((host, port)) # conecta ao servidor

def enviar():
    while True:
        msg = input("Digite a mensagem: ")
        clie.send(msg.encode("utf-8")) # codifica a mensagem para bits

Thread(target=enviar).start()