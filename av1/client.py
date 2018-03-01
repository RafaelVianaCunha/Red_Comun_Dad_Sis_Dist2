import socket

#servidor
IP_server='localhost'
porta_server=12397

socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#socket_cliente.bind((IP,porta))

palpite = input('Qual o seu palpite: ')

while (palpite != 'sair'):
    socket_cliente.sendto(palpite.encode('utf-8'), (IP_server, porta_server))

    rec, addr = socket_cliente.recvfrom(1024)
    print(rec.decode('utf-8'))

    palpite = input('Qual o seu palpite: ')

socket_cliente.close()  