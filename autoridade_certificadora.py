from socket import socket, AF_INET, SOCK_DGRAM
from threading import Thread
import time

class AC:
    def __init__(self, nome, porta = 12345):
        # Preparando informações de AC:
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
        # Buffer
        self.buffer = []
        # Thread:
        self.thread = Thread(target=self.rodando, args=())
        self.thread.start()

    def rodando(self):
        time.sleep(5)
        print(self.con_1)
        print(self.con_2)
        print(self.con_3)
        print(self.con_4)
        print(self.con_5)
        print(self.con_6)
    
    def rede(self):
        mensagem_recebida, endereco_remetente = self.socket.recvfrom(2048)
        mensagem_recebida = mensagem_recebida.decode()
        self.buffer_add(mensagem_recebida)
    
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
        set_com = getattr(ac, f"set_con_{con_num}")
        set_com(pc.endereco_servidor)