import socket , pickle

class Resposta:
    def __init__(self, palavra, erros):
        self.palavra = palavra
        self.erros = erros

def print_error(erros):
    if (erros == 1):
        print(""" 
                 ___________
                 |          |
                 |         ---
                 |          O
                 | 
                 |
                 |
                ---
              """)
        return
    if (erros == 2):
        print(""" 
                 ___________
                 |          |
                 |         ---
                 |          O
                 |          |
                 |
                 |
                ---
              """)
        return
    if (erros == 3):
        print(""" 
                 ___________
                 |          |
                 |         ---
                 |          O
                 |         /|
                 |
                 |
                ---
              """)
        return
    if (erros == 4):
        print(""" 
                 ___________
                 |          |
                 |         ---
                 |          O
                 |         /|\\
                 |
                 |
                ---
              """)
        return
    if (erros == 5):
        print(""" 
                 ___________
                 |          |
                 |         ---
                 |          O
                 |         /|\\
                 |         /
                 |
                ---
              """)
        return
    if (erros == 6):
        print(""" 
                 ___________
                 |          |
                 |         ---
                 |          O
                 |         /|\\
                 |         / \\
                 |
                ---
              """)
        return
    if (erros == 7):
        print(""" 
                 ___________
                 |          |
                 |         ---
                 |          O
                 |         ---
                 |         /|\\
                 |         / \\
                 |
                ---
              """)
        return

#servidor
IP_server='localhost'
porta_server=12397

socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#socket_cliente.bind((IP,porta))

socket_cliente.sendto('start'.encode('utf-8'), (IP_server, porta_server))
while (True):
    rec, addr = socket_cliente.recvfrom(1024)
    data = pickle.loads(rec)

    if (data.palavra != ''):
        print(data.palavra + '\n')
        break

palpite = input('Qual o seu palpite: ')

while (palpite != 'sair'):
    socket_cliente.sendto(palpite[0].encode('utf-8'), (IP_server, porta_server))

    rec, addr = socket_cliente.recvfrom(1024)
    data = pickle.loads(rec)
    # print(rec.decode('utf-8'))

    print(data.palavra + '\n')

    print_error(data.erros)    

    if (data.erros == 7):
        print('Voce perdeu :(')
        break

    if ('_' not in data.palavra):
        print('Parabens! Você ganhou')
        break

    palpite = input('Qual o seu palpite: ')

socket_cliente.close()  

