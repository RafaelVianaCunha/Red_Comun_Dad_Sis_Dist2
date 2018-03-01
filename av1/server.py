import socket
import random

#servidor
IP='localhost'
porta=12397

arquivo = open('palavras.txt', 'r') 
palavras =  arquivo.readlines()

socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

socket_servidor.bind((IP,porta))

palavra = random.choices(palavras)[0].lower().replace('\n', '')

erros = 0

print(palavra)

palpites = []

while (True):
    palpite, addr = socket_servidor.recvfrom(1024)
    palpite = palpite.decode('utf-8').lower()
    palpites.append(palpite)

    print (palpite)

    if (palpite not in palavra):
        erros = erros + 1
    
    retorno = ''

    for letra in palavra:
        if (letra in palpites):
            retorno = retorno + letra + ' '
        else:
            retorno = retorno + ' _ '

    socket_servidor.sendto(retorno.encode('utf-8'), addr)

socket_servidor.close()
