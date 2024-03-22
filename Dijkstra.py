import sys
import geral as g

class Roteamento():
    def __init__(self, origem):
        self.origem = origem
        self.tabela = {
            'PC1': None,
            'PC2': None,
            'PC3': None,
            'PC4': None,
            'PC5': None,
            'PC6': None
        }
        self.tabela_enderecos = {}
        self.grafo = {
        'PC1': {'PC2': 1, 'PC6': 1},
        'PC2': {'PC1': 1, 'PC3': 1},
        'PC3': {'PC2': 1, 'PC4': 1},
        'PC4': {'PC3': 1, 'PC5': 1},
        'PC5': {'PC4': 1, 'PC6': 1},
        'PC6': {'PC5': 1, 'PC1': 1}
        }
        self.lista_visitados = []

    def criar_tabela_forwarding(self):
        self.reset_valores()
        self.calcular_dijkstra()
        self.preenche_tabela()
        self.montar_tabela_com_enderecos()
        return self.tabela_enderecos

    def reset_valores(self):
        self.tabela = {
            'PC1': None,
            'PC2': None,
            'PC3': None,
            'PC4': None,
            'PC5': None,
            'PC6': None
        }
        self.tabela_enderecos = {}
        self.lista_visitados = []

    # Função do algoritmo de Dijkstra
    def calcular_dijkstra(self):
        origem = self.origem
        grafo = self.grafo
        # Inicialização das distâncias com infinito, exceto a origem que é zero
        distancias = {v: sys.maxsize for v in grafo}
        distancias[origem] = 0

        # Conjunto de vértices visitados
        visitados = set()

        while visitados != set(distancias):
            # Encontra o vértice não visitado com menor distância atual
            vertice_atual = None
            menor_distancia = sys.maxsize
            for v in grafo:
                if v not in visitados and distancias[v] < menor_distancia:
                    vertice_atual = v
                    menor_distancia = distancias[v]
                    
            # Marca o vértice atual como visitado
            visitados.add(vertice_atual)

            # Atualiza as distâncias dos vértices vizinhos
            for vizinho, peso in grafo[vertice_atual].items():
                if distancias[vertice_atual] + peso < distancias[vizinho]:
                    distancias[vizinho] = distancias[vertice_atual] + peso
                    self.lista_visitados.append((vertice_atual, vizinho))

        # Retorna as distâncias mais curtas a partir da origem
        return distancias

    # Preenche a tabela de encaminhamento.
    def preenche_tabela(self):
        for k in self.tabela.keys():
            mandar_para = self.percorrer(k, self.lista_visitados)
            self.tabela[k] = mandar_para
        #print(self.tabela)
    
    # Percorre o caminho do destino até a origem para descobrir pra qual nó tem que ir a partir da origem.
    def percorrer(self, destino, lista):
        origem = 0
        for dupla in lista:
            if destino == dupla[1]:
                origem = dupla[0]
                if origem == self.origem:
                    return destino
                else:
                    return self.percorrer(origem, lista)
    
    # Muda os nomes na tabela pelos endereços.
    def montar_tabela_com_enderecos(self):
        for k in self.tabela.keys():
            chave_endereco = g.enderecos[k]
            valor = self.tabela[k]
            valor_endereco = None
            if valor != None:
                valor_endereco = g.enderecos[valor]
            self.tabela_enderecos[chave_endereco] = valor_endereco

'''x = Roteamento("PC1")
x.exibir_caminhos()
x.preenche_tabela()'''

'''# Exibe os caminhos mais curtos encontrados
    def exibir_caminhos(self):
        caminhos_mais_curto = self.calcular_dijkstra()
        for destino, distancia in caminhos_mais_curto.items():
            print(f"Caminho mais curto de {self.origem} para {destino}: {distancia}")'''