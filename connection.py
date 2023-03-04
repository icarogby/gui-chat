import socket

class Connection():
        host = "177.71.139.240" # ip do servidor na AWS
        port = 5000

        clie = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET = IPV4 | SOCK_STREAM = TCP
        clie.connect((host, port)) # conecta ao servidor

        def nome(self, nome):
                self.clie.send(f"{nome}".encode("utf-8")) # codifica a mensagem para bits

        def enviar(self, msg = "", window = None):
                if msg == "":
                        return
                
                window.msg_list.addItem(f"Você: {msg}")
                self.clie.send(msg.encode("utf-8")) # codifica a mensagem para bits

        def receber(self, window):
                while True:
                        msg = self.clie.recv(1024).decode("utf-8") # 1024 = tamanho do buffer

                        if not msg:
                                break

                        window.msg_list.addItem(msg)
