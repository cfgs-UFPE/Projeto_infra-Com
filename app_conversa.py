from mensagem import *
import geral as g
from threading import Thread

class APP:
    def __init__(self, nome, c1, c2, c3, c4, c5):
        self.nome = nome
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
        self.esperando_resposta = {}
        self.prepara_esperando_resposta()
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
            if self.pode_mandar_mensagem():
                self.mandar_mensagens(self.pc)

    # Manda 5 mensagens, uma para cada contato.
    def mandar_mensagens(self, pc):
        for i in range(1,6):
            # Prepara informações.
            contato = getattr(self, f"contato_{i}")
            papo = getattr(self, f"papo_{i}")
            n = self.numero_da_mensagem(papo)
            texto = "MSG" + str(n) #texto = input("Teste:")
            # Cria a mensagem.
            divisor = g.divisor_dados
            dados = self.nome + divisor + "msg" + divisor + texto
            m = Mensagem(TipoMensagem.APP, pc.endereco_servidor, g.enderecos[contato], dados)
            # Adiciona mensagem a conversa.
            papo.append([self.nome, texto])
            self.esperando_resposta[contato] = True
            # Mada mensagem para a lista de mensagens de pc, para que ele envie a mensagem.
            pc.add_mensagem_lista(m)

    # Recebe as informações das mensagens que pc encaminhar para o app e registra em uma das conversas (papos).
    def receber_mensagens(self, mensagem):
        pass
    
    # Preenche o dicionario esperando_resposta.
    def prepara_esperando_resposta(self):
        self.esperando_resposta[self.contato_1] = False
        self.esperando_resposta[self.contato_2] = False
        self.esperando_resposta[self.contato_3] = False
        self.esperando_resposta[self.contato_4] = False
        self.esperando_resposta[self.contato_5] = False
    
    # Verifica se pode mandar novas mensagens, só vai ser true se não estiver esperando resposta de nenhum contato.
    def pode_mandar_mensagem(self):
        valor = True
        for k in self.esperando_resposta.keys():
            if self.esperando_resposta[k] == True:
                valor = False
                break
        return valor
    
    def numero_da_mensagem(self, papo):
        contador = 0
        for m in papo:
            if m[0] == self.nome:
                contador += 1
        return contador