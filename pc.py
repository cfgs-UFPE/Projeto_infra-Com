from mensagem import *
from app_conversa import *
from Dijkstra import *
import geral as g
from socket import socket, AF_INET, SOCK_DGRAM
from threading import Thread
import criptar
import time

class PC:
    def __init__(self, nome, endereco, app_conversa):
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
        # Roteamento:
        self.roteamento = Roteamento(self.nome)
        self.tabela_forwarding = self.roteamento.criar_tabela_forwarding()
        # Chaves privada:
        self.chave_privada = None
        # Listas de mensagens:
        self.mensagens_lista = []
        self.mensagens_encriptar_lista = []
        # APP:
        self.app = app_conversa
        # Thread:
        self.thread_receber_mensagens = Thread(target=self.receber, args=())
        self.thread_rodando = Thread(target=self.rodando, args=())
    
    # Inicia o PC, fazendo ele se regstrar na AC, inicia suas threads e app. 
    def iniciar(self):
        self.registrar_em_ac()
        self.thread_rodando.start()
        self.thread_receber_mensagens.start()
        self.app.iniciar(self)

    # # Thread que fica em loop tratando as mensagens da lista de mensagens.
    def rodando(self):
        while True:
            if len(self.mensagens_lista) > 0:
                m = self.mensagens_lista[0]
                if isinstance(m, Mensagem):
                    # Mensagem não é para esse PC: manda para onde tem que ir
                    if m.get_destino_endereco() != self.endereco_servidor:
                            m_string = m.info_para_string()
                            if m.get_destino_endereco() == self.con_ac:
                                self.socket.sendto(m_string.encode(), self.con_ac)
                            elif m.tipo == TipoMensagem.ENCRIPTAR:
                                self.mensagens_encriptar_lista.append(m)
                                destino = m.get_destino_endereco()
                                dados = destino[0] + str(destino[1])
                                m_pede_chave = Mensagem(TipoMensagem.PEDIDO_CHAVE_PUBLICA, self.endereco_servidor, self.con_ac, dados)
                                self.add_mensagem_lista(m_pede_chave)
                            else:
                                mandar_para = self.tabela_forwarding[m.get_destino_endereco()]
                                com_num = self.coneccao_por_endereco(mandar_para)
                                if com_num == TipoCon.CON_1:
                                    self.socket.sendto(m_string.encode(), self.con_1)
                                if com_num == TipoCon.CON_2:
                                    self.socket.sendto(m_string.encode(), self.con_2)
                                # *teste* print(f"mandou por com_{com_num}")
                    # Mensagem é para esse PC: trata de acordo com o tipo.
                    else:
                        if m.tipo == TipoMensagem.CHAVE_PRIVADA:
                                self.chave_privada = self.string_para_chave(m.dados)
                                # *teste* print(f"{self.nome} : recebeu chave privada {self.chave_privada} de {m.get_origem_endereco()}.")
                        elif m.tipo == TipoMensagem.APP:
                            if m.get_destino_endereco() == self.endereco_servidor:
                                self.app.receber_mensagens(m.dados)
                self.mensagens_lista.pop(0)


    # Thread que fica em loop recebendo as mensagens e mandando para a lista de mensagens.
    def receber(self):
        while True:
            # Recebe mensagem.
            mensagem_recebida, endereco_remetente = self.socket.recvfrom(2048)
            mensagem_recebida = mensagem_recebida.decode()
            # transformar a mensagem recebida em um objeto Mensagem.
            m = Mensagem()
            m.string_para_info(mensagem_recebida)
            # Adiciona mensagem a lista.
            self.add_mensagem_lista(m)
    
    # Faz PC se registrar na Autoridade Certificadora.
    def registrar_em_ac(self):
        if self.con_ac != None:
            m = Mensagem(TipoMensagem.CRIAR_CHAVE, self.endereco_servidor, self.con_ac)
            self.add_mensagem_lista(m)

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
    
    # Retorna a conecção por endereco.
    def coneccao_por_endereco(self, endereco):
        if endereco == self.con_1:
            return TipoCon.CON_1
        elif endereco == self.con_2:
            return TipoCon.CON_2
        elif endereco == self.con_ac:
            return TipoCon.CON_AC

    # Converte a string de uma chave em uma chave.
    def string_para_chave(self, string):
        divisor = g.divisor_dados
        s = string.split(divisor)
        info = []
        for i in range(1, len(s)):
            info.append(int(s[i]))
        if s[0] == "Privada":
            chave = criptar.rsa.PrivateKey(info[0], info[1], info[2], info[3], info[4])
        elif s == "Publica":
            chave = criptar.rsa.PublicKey(info[0], info[1])
        return chave

    # Adiciona uma mensagem ao buffer.
    def add_mensagem_lista(self, mensagem):
        if isinstance(mensagem, Mensagem):
            self.mensagens_lista.append(mensagem)

# Enum das conexões de PC.
class TipoCon():
    CON_1 = 1
    CON_2 = 2
    CON_AC = 3  