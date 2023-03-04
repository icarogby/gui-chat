import socket
from threading import Thread

listacon: list[socket.socket] = []
listanomes = {}

host = socket.gethostbyname(socket.gethostname())
port = 5000

print(f"HOST: {host}, PORT: {port}")

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET = IPV4 | SOCK_STREAM = TCP
serv.bind((host, port)) # bind = vincular
serv.listen(5) # limites de conexões

def servidor():
    global listacon
    global listanomes
    nome = ""

    while True:
        con, adr = serv.accept() # aceita conexão
        listacon.append(con)

        while True:
            msg = con.recv(1024) # 1024 = tamanho do buffer

            if not msg:
                listacon.remove(con)
                listanomes.pop(con)
                break
            
            msg = msg.decode("utf-8")

            if nome == "":
                nome = msg
                listanomes[con] = nome
                msg = f"{nome} entrou na sala"
            else:
                msg = f"{listanomes[con]}: {msg}"

            print(msg)

            for i in range(len(listacon)):
                if listacon[i] != con:
                    listacon[i].sendall(msg.encode("utf-8"))

for i in range(5):
    Thread(target=servidor).start()
