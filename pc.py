from socket import socket, AF_INET, SOCK_DGRAM
from threading import Thread
from mensagem import *
import time
import rsa

class PC:
    def __init__(self, nome, porta = 12345):
        # Preparando informações de PC:
        self.nome = nome
        self.nome_servidor = 'localhost'
        self.porta_servidor = porta
        self.endereco_servidor = (self.nome_servidor, self.porta_servidor)
        # Socket:
        self.socket = socket(AF_INET, SOCK_DGRAM)
        self.socket.bind(self.endereco_servidor)
        # conexões:
        self.con_1 = None
        self.con_2 = None
        self.con_ac = None
        # Chaves privada:
        self.chave = None
        # Thread:
        self.thread = Thread(target=self.rodando, args=())
    
    def iniciar(self):
        self.thread.start()

    def rodando(self):
        self.registrar_em_ac()
        while True:
            mensagem_recebida, endereco_remetente = self.socket.recvfrom(2048)
            mensagem_recebida = mensagem_recebida.decode()
            #print(f"{self.nome} : {mensagem_recebida} de {endereco_remetente}")

    def buffer_add(self, mensagem):
        self.buffer.append(mensagem)
    
    def registrar_em_ac(self):
        if self.con_ac != None:
            m = Mensagem(Tipo.CRIAR_CHAVE, self.endereco_servidor, self.con_ac)
            m_string = m.info_para_string()
            self.socket.sendto(m_string.encode(), self.con_ac)

    def set_con_1(self, con):
        self.con_1 = con
    
    def set_con_2(self, con):
        self.con_2 = con
    
    def set_con_ac(self, ac):
        self.con_ac = ac

def conectar_pc_pc(pc1, pc2):
    pc1.set_con_2(pc2.endereco_servidor)
    pc2.set_con_1(pc1.endereco_servidor)