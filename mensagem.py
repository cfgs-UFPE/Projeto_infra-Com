class Mensagem:
    def __init__(self, tipo=None, origem_endereco=None, destino_endereco=None, dados=None):
        # Informações da mensagem:
        self.tipo = None
        self.origem_nome_servidor = None
        self.origem_porta_servidor = None
        self.destino_nome_servidor = None
        self.destino_porta_servidor = None
        self.dados = None
        self.set_tipo(tipo)
        self.set_origem_endereco(origem_endereco)
        self.set_destino_endereco(destino_endereco)
        self.set_dados(dados)
        # Variaveis internas:
        self.divisor = "*-*"

    # Converte as informações da mensagem em uma string.
    def info_para_string(self):
        s = ""
        informacoes = [self.tipo, self.origem_nome_servidor, self.origem_porta_servidor,
                       self.destino_nome_servidor, self.destino_porta_servidor, self.dados]
        for i in informacoes:
            s = s + self.divisor + str(i)
        s = s.removeprefix(self.divisor)
        return s

    # Converte uma string para as informações da mensagem. 
    def string_para_info(self, string):
        s = string.split(self.divisor)
        informacoes = ["tipo", "origem_nome_servidor", "origem_porta_servidor",
                       "destino_nome_servidor", "destino_porta_servidor", "dados"]
        for i in range(len(informacoes)):
            info = informacoes[i]
            set_info = getattr(self, f"set_{info}")
            set_info(s[i])
    
    # - Sets:
    def set_tipo(self, valor_tipo):
        if valor_tipo == None:
            self.tipo = TipoMensagem.NADA
        else:
            if isinstance(valor_tipo, int):
                self.tipo = valor_tipo
            elif isinstance(valor_tipo, str):
                self.tipo = int(valor_tipo)

    def set_origem_endereco(self, origem_endereco):
        if origem_endereco != None:
            self.set_origem_nome_servidor(origem_endereco[0])
            self.set_origem_porta_servidor(origem_endereco[1])

    def set_origem_nome_servidor(self, valor_origem_nome_servidor):
        self.origem_nome_servidor = valor_origem_nome_servidor
    
    def set_origem_porta_servidor(self, valor_origem_porta_servidor):
        self.origem_porta_servidor = valor_origem_porta_servidor
    
    def set_destino_endereco(self, destino_endereco):
        if destino_endereco != None:
            self.set_destino_nome_servidor(destino_endereco[0])
            self.set_destino_porta_servidor(destino_endereco[1])

    def set_destino_nome_servidor(self, valor_destino_nome_servidor):
        self.destino_nome_servidor = valor_destino_nome_servidor
    
    def set_destino_porta_servidor(self, valor_destino_porta_servidor):
        self.destino_porta_servidor = valor_destino_porta_servidor
    
    def set_dados(self, valor_dados):
        self.dados = valor_dados

class TipoMensagem():
    NADA = 0
    CRIAR_CHAVE = 1