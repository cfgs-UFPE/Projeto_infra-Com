from mensagem import *
import geral as g
from threading import Thread
import os

class APP:
    def __init__(self, nome, c1, c2, c3, c4, c5):
        # Informações de uso:
        self.nome = nome
        # Estados:
        self.estado_atual = EstadosApp.INICIO
        self.conversa_atual = None
        # Contatos com quem tá conversando:
        self.contato_1 = c1
        self.contato_2 = c2
        self.contato_3 = c3
        self.contato_4 = c4
        self.contato_5 = c5
        self.contatos_lista = [self.contato_1, self.contato_2, self.contato_3, self.contato_4, self.contato_5]
        # Dados das conversas:
        self.papo_1 = []
        self.papo_2 = []
        self.papo_3 = []
        self.papo_4 = []
        self.papo_5 = []
        self.papos_lista = [self.papo_1, self.papo_2, self.papo_3, self.papo_4, self.papo_5]
        '''self.esperando_resposta = {}
        self.prepara_esperando_resposta()'''
        # PC:
        self.pc = None
        # Thread:
        self.thread_rodando = Thread(target=self.rodando, args=())
    
    # Inicia o app.
    def iniciar(self, pc_rodando):
        self.pc = pc_rodando
        self.thread_rodando.start()

    # Thread que fica em loop executando o que o app tem que fazer.
    def rodando(self):
        loop = True
        while loop:
            # Print:
            self.titulo_print()
            if self.estado_atual == EstadosApp.INICIO:
                self.estado_inicio_print()
            elif self.estado_atual == EstadosApp.CONVERSA:
                self.estado_conversa_print()
            # Comando:
            comando = input(" > ")
            comando = comando.lower()
            if self.estado_atual == EstadosApp.INICIO:
                self.estado_inicio_comandos(comando)
            elif self.estado_atual == EstadosApp.CONVERSA:
                self.estado_conversa_comandos(comando)
    
    # -- Rodando aplicação:
    # - Prints:
    def titulo_print(self):
        os.system("cls")
        print(" -- APP CONVERSAS --")

    def estado_inicio_print(self):
            print(" CONVERSAS")
            print()
            for i in range(len(self.contatos_lista)):
                print(f" {i+1} - " + self.contatos_lista[i])
            print()
            print(" Comandos:")
            print(" - <entrar x> -> entra na conversa de número x.")
            print()
            print()
    
    def estado_conversa_print(self):
        print(f" CONVERSA COM {self.contatos_lista[self.conversa_atual]}")
        print()
        papo = self.papos_lista[self.conversa_atual]
        for m in papo:
            autor = m[0]
            texto = m[1]
            print(f" {autor}: {texto}")
        print()
        print(" Comandos:")
        print(" - <sair> -> sai da conversa e volta para a lista de contatos.")
        print(" - <msg> -> comando para mandar uma mensagem.")
        print()
        print()

    # - Comandos:
    def estado_inicio_comandos(self, comando):
        lista_comando = comando.split(" ")
        if len(lista_comando) == 2:
            if lista_comando[0] == "entrar":
                if lista_comando[1].isdigit():
                    numero = int(lista_comando[1])
                    if numero >= 1 and numero <= 5:
                        self.conversa_atual = numero - 1
                        self.estado_atual = EstadosApp.CONVERSA
                        # *teste* print(self.conversa_atual)
                        # *teste* input()
    
    def estado_conversa_comandos(self, comando):
        if comando == "sair":
            self.estado_atual = EstadosApp.INICIO
        elif comando == "msg":
            print()
            texto = input(" Escreva sua mensagem: ")
            self.mandar_mensagens(self.pc, self.conversa_atual, texto)

    # Mensagens:
    # Manda mensagem para contato que está conversando.
    def mandar_mensagens(self, pc, conversa, mensagem):
        # Prepara informações.
        contato = self.contatos_lista[conversa]
        papo = self.papos_lista[conversa]
        # Cria a mensagem.
        divisor = g.divisor_dados
        dados = self.nome + divisor + mensagem
        m = Mensagem(TipoMensagem.APP, pc.endereco_servidor, g.enderecos[contato], dados)
        # Adiciona mensagem a conversa.
        papo.append([self.nome, mensagem])
        # Mada mensagem para a lista de mensagens de pc, para que ele envie a mensagem.
        pc.add_mensagem_lista(m)

    # Recebe as mensagens que pc encaminhar para o app e guarda em uma das conversas (papos).
    def receber_mensagens(self, mensagem):
        divisor = g.divisor_dados
        m = mensagem.split(divisor)
        conversa = self.identificar_conversa(m[0])
        self.papos_lista[conversa].append(m)
        if self.estado_atual == EstadosApp.CONVERSA:
            self.titulo_print()
            self.estado_conversa_print()
            print(" > ", end="")
    
    # Retorna o número da conversa de acordo com o contato.
    def identificar_conversa(self, contato):
        if contato == self.contato_1:
            return 0
        elif contato == self.contato_2:
            return 1
        elif contato == self.contato_3:
            return 2
        elif contato == self.contato_4:
            return 3
        elif contato == self.contato_5:
            return 4

class EstadosApp:
    INICIO = 0
    CONVERSA = 1