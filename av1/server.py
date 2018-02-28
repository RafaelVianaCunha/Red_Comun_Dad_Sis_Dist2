import socket

class Jogo:
    def __init__(self):
        _file = open(palavras.txt”, “r”) 
        self.palavras =  file.readlines()

    def novoJogo(self, trick):
        


#servidor
IP='localhost'
porta=12397

socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

socket_servidor.bind((IP,porta))

mgs, addr= socket_servidor.recvfrom(1024)
print (mgs,addr)

socket_servidor.sendto(b'recebido',addr)


socket_servidor.close()