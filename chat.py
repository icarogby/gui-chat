import socket
from threading import Thread

host = socket.gethostbyname(socket.gethostname())
port = 2000

print(f"HOST: {host}, PORT: {port}")

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET = IPV4 | SOCK_STREAM = TCP
serv.bind((host, port)) # bind = vincular
serv.listen(5) # limites de conexões

def receber():
    while True:
        con, adr = serv.accept() # aceita conexão

        while True:
            msg = con.recv(1024) # 1024 = tamanho do buffer

            if not msg:
                break

            print(msg.decode("utf-8")) # decodifica a mensagem pq vem em bits


Thread(target=receber).start()