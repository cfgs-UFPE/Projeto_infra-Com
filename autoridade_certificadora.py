from mensagem import *
import geral as g
from socket import socket, AF_INET, SOCK_DGRAM
from threading import Thread
import rsa
import time

class AC:
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
        self.con_3 = None
        self.con_4 = None
        self.con_5 = None
        self.con_6 = None
        # Chaves publicas:
        self.chaves_dict = {}
        # Thread:
        self.thread_receber_mensagens = Thread(target=self.receber, args=())
    
    # Inicia a thread de AC. 
    def iniciar(self):
        self.thread_receber_mensagens.start()

    # # Thread que fica em loop recebendo e tratando as mensagens.
    def receber(self):
        while True:
            # Recebe mensagem.
            mensagem_recebida, endereco_remetente = self.socket.recvfrom(2048)
            mensagem_recebida = mensagem_recebida.decode()
            # transformar a mensagem recebida em um objeto Mensagem.
            m = Mensagem()
            m.string_para_info(mensagem_recebida)
            # Trata as mensagens de acordo com o tipo.
            if m.tipo == TipoMensagem.CRIAR_CHAVE:
                # *teste* print(f"{self.nome} : {endereco_remetente} pediu para \'CriarChave\'.")
                self.faz_registro(endereco_remetente)
    
    # - Registrar PC:
    # Executa as funções que fazem o registro de PC em AC: cria as chaves, armazena a chave publica
    # e envia a chave privada.
    def faz_registro(self, endereco):
        chave_publica, chave_privada = self.criar_chave()
        self.armazenar_chave_publica(chave_publica, endereco)
        self.envia_chave_privada(chave_privada, endereco)

    # Função que cria as chaves publica e privada.
    def criar_chave(self):
        c_priv, c_pub = rsa.gerar_chaves()
        return c_pub, c_priv
    
    # Função que armazena a chave publica em um dicionario onde a chave é o endereço do PC.
    def armazenar_chave_publica(self, chave_publica, endereco_pc):
        self.chaves_dict[endereco_pc] = chave_publica
    
    # Função que envia a chave privada para o PC.
    def envia_chave_privada(self, chave_privada, endereco_pc):
        chave_string = self.chave_para_string(chave_privada)
        m = Mensagem(TipoMensagem.CHAVE_PRIVADA, self.endereco_servidor, endereco_pc, chave_string)
        m_string = m.info_para_string()
        self.socket.sendto(m_string.encode(), endereco_pc)
        # *teste* print(f"{self.nome} : Mandou chave {chave_privada} para {endereco_pc}.")

    # - Sets:
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

    # Conecta a AC a um endereço.
    def ac_conectar(self, tipo, endereco):
        if tipo == TipoCon.CON_1:
            self.set_con_1(endereco)
        elif tipo == TipoCon.CON_2:
            self.set_con_2(endereco)
        elif tipo == TipoCon.CON_3:
            self.set_con_3(endereco)
        elif tipo == TipoCon.CON_4:
            self.set_con_4(endereco)
        elif tipo == TipoCon.CON_5:
            self.set_con_5(endereco)
        elif tipo == TipoCon.CON_6:
            self.set_con_6(endereco)

    # Converte uma chave para uma string.
    def chave_para_string(self, chave):
        divisor = g.divisor_dados
        s = ""
        if isinstance(chave, rsa.PrivateKey):
            s = "Privada"
            informacoes = [chave.n, chave.e, chave.d, chave.p, chave.q]
            for info in informacoes:
                s = s + divisor + str(info)
        elif isinstance(chave, rsa.PublicKey):
            s = "Publica"
            informacoes = [chave.n, chave.e]
            for info in informacoes:
                s = s + divisor + str(info)
        return s

# Enum das conexões de AC.
class TipoCon():
    CON_1 = 1
    CON_2 = 2
    CON_3 = 3
    CON_4 = 4
    CON_5 = 5
    CON_6 = 6