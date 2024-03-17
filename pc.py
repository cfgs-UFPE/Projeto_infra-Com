from mensagem import *
from socket import socket, AF_INET, SOCK_DGRAM
from threading import Thread
import rsa
import time

class PC:
    def __init__(self, nome, endereco):
        # Preparando informações de PC:
        self.nome = nome
        self.endereco_servidor = endereco
        self.nome_servidor = self.endereco_servidor[0]
        self.porta_servidor = self.endereco_servidor[1]
        # Socket:
        self.socket = socket(AF_INET, SOCK_DGRAM)
        self.socket.bind(self.endereco_servidor)
        # conexões:
        self.con_1 = None
        self.con_2 = None
        self.con_ac = None
        # Chaves privada:
        self.chave_privada = None
        # Thread:
        self.thread_receber_mensagens = Thread(target=self.receber, args=())
    
    # Inicia o PC, fazendo ele se regstrar na AC e e iniciando suas threads. 
    def iniciar(self):
        self.registrar_em_ac()
        self.thread_receber_mensagens.start()

    # Thread que fica recebendo as mensagens.
    def receber(self):
        while True:
            # Recebe mensagem.
            mensagem_recebida, endereco_remetente = self.socket.recvfrom(2048)
            mensagem_recebida = mensagem_recebida.decode()
            # transformar a mensagem recebida em um objeto Mensagem.
            m = Mensagem()
            m.string_para_info(mensagem_recebida)
            # Trata as mensagens de acordo com o tipo.
            if m.tipo == TipoMensagem.CHAVE_PRIVADA:
                self.chave_privada = self.string_para_chave(m.dados)
                #print(f"{self.nome} : recebeu chave privada {self.chave_privada} de {endereco_remetente}.")
    
    # Faz PC se registrar na Autoridade Certificadora.
    def registrar_em_ac(self):
        if self.con_ac != None:
            m = Mensagem(TipoMensagem.CRIAR_CHAVE, self.endereco_servidor, self.con_ac)
            m_string = m.info_para_string()
            self.socket.sendto(m_string.encode(), self.con_ac)

    # - Sets:
    def set_con_1(self, con):
        self.con_1 = con
    
    def set_con_2(self, con):
        self.con_2 = con
    
    def set_con_ac(self, ac):
        self.con_ac = ac

    # Conecta o PC a um endereço.
    def pc_conectar(self, tipo, endereco):
        if tipo == TipoCon.CON_1:
            self.set_con_1(endereco)
        elif tipo == TipoCon.CON_2:
            self.set_con_2(endereco)
        elif tipo == TipoCon.CON_AC:
            self.set_con_ac(endereco)
    
    # Converte a string de uma chave em uma chave.
    def string_para_chave(self, string):
        divisor = "---"
        s = string.split(divisor)
        info = []
        for i in range(1, len(s)):
            info.append(int(s[i]))
        if s[0] == "Privada":
            chave = rsa.PrivateKey(info[0], info[1], info[2], info[3], info[4])
        elif s == "Publica":
            chave = rsa.PublicKey(info[0], info[1])
        return chave

# Enum das conexões de PC.
class TipoCon():
    CON_1 = 1
    CON_2 = 2
    CON_AC = 3  