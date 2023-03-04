import socket
from threading import Thread

listacon: list[socket.socket] = []

host = socket.gethostbyname(socket.gethostname())
port = 5000

print(f"HOST: {host}, PORT: {port}")

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET = IPV4 | SOCK_STREAM = TCP
serv.bind((host, port)) # bind = vincular
serv.listen(5) # limites de conexões

def servidor():
    global listacon

    while True:
        con, adr = serv.accept() # aceita conexão
        listacon.append(con)

        while True:
            msg = con.recv(1024) # 1024 = tamanho do buffer

            if not msg:
                listacon.remove(con)
                break
            
            for i in range(len(listacon)):
                if listacon[i] != con:
                    listacon[i].sendall(msg)
            
            

for i in range(5):
    Thread(target=servidor).start()
