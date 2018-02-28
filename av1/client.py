import socket

#servidor
IP_server='localhost'
porta_server=12397

socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#socket_cliente.bind((IP,porta))
MSG="to enviando!"
socket_cliente.sendto(MSG.encode('ascii'), (IP_server,porta_server))

rec=socket_cliente.recvfrom(1024)
print(rec)

socket_cliente.close()