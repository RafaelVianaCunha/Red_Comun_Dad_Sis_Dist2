import socket , pickle , random

class Resposta:
    def __init__(self, palavra, erros):
        self.palavra = palavra
        self.erros = erros

#servidor
IP='localhost'
porta=12397

class Jogo:
    def __init__(self):
        arquivo = open('palavras.txt', 'r') 
        self.palavras =  arquivo.readlines()
        self.Tot_erro = 7
        self.erros = 0
    def novoJogo(self):
        print("Novo Jogo")
        self.socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket_servidor.bind((IP,porta))
        self.palavra = random.choices(self.palavras)[0].lower().replace('\n', '')
        self.erros = 0
        print(self.palavra)

        start, addr = self.socket_servidor.recvfrom(1024)
        start = start.decode('utf-8').lower()

        while (start != 'start'):
            start, addr = self.socket_servidor.recvfrom(1024)
            start = start.decode('utf-8').lower()
        
        palavraEscondida = ''
        for letra in self.palavra:
            palavraEscondida = palavraEscondida + '_ '

        reposta = Resposta(palavraEscondida, self.erros)
        data_string = pickle.dumps(reposta)
        self.socket_servidor.sendto(data_string, addr)

        self.palpites = []
        self.main()

    def main(self):
        while (self.erros<=(self.Tot_erro-1)):
            palpite, addr = self.socket_servidor.recvfrom(1024)
            palpite = palpite.decode('utf-8').lower()
            self.palpites.append(palpite)

            print (palpite)
           
            if (palpite not in self.palavra):
                self.erros = self.erros + 1
            
            retorno = ''

            for letra in self.palavra:
                if (letra in self.palpites):
                    retorno = retorno + letra + ' '
                else:
                    retorno = retorno + ' _ '
            
            reposta = Resposta(retorno, self.erros)
            data_string = pickle.dumps(reposta)
            self.socket_servidor.sendto(data_string, addr)
            if ('_' not in retorno):
                print('Ganhou')
                return

        self.novoJogo()

    def fimDeJogo(self):
        self.socket_servidor.close()

jogo = Jogo()
jogo.novoJogo()
jogo.fimDeJogo()
