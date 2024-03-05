from socket import socket, AF_INET, SOCK_DGRAM
from threading import Thread
from mensagem import *
import time
import rsa

class AC:
    def __init__(self, nome, porta = 12345):
        # Preparando informações de AC:
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
        self.con_3 = None
        self.con_4 = None
        self.con_5 = None
        self.con_6 = None
        # Chaves publicas:
        self.chaves_dict = {}
        # Thread:
        self.thread = Thread(target=self.rodando, args=())

    def iniciar(self):
        self.thread.start()

    def rodando(self):
        while True:
            mensagem_recebida, endereco_remetente = self.socket.recvfrom(2048)
            mensagem_recebida = mensagem_recebida.decode()
            m = Mensagem()
            m.string_para_info(mensagem_recebida)
            if m.tipo == Tipo.CRIAR_CHAVE:
                self.faz_registro(endereco_remetente)
                print(f"{self.nome} : pedido \'\'CriarChave\'\' de {endereco_remetente}")
    
    def faz_registro(self, endereco):
        chave_publica, chave_privada = self.criar_chave()
        #self.socket.sendto(chave_privada, endereco)

    def criar_chave(self):
        c_pub, c_priv = rsa.newkeys(320)
        return c_pub, c_priv

    def buffer_add(self, mensagem):
        self.buffer.append(mensagem)

    def set_con_1(self, con):
        self.con_1 = con
    
    def set_con_2(self, con):
        self.con_2 = con
    
    def set_con_3(self, con):
        self.con_3 = con
    
    def set_con_4(self, con):
        self.con_4 = con
    
    def set_con_5(self, con):
        self.con_5 = con
    
    def set_con_6(self, con):
        self.con_6 = con

def conectar_PC_AC(pc, ac, con_num):
    if isinstance(con_num, int) and con_num >= 1 and con_num <= 6:
        set_con = getattr(ac, f"set_con_{con_num}")
        set_con(pc.endereco_servidor)
        pc.con_ac = ac.endereco_servidor