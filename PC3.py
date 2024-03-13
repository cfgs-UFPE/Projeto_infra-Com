from pc import *
import Inicializacao
import os

nome = "PC3"
endereco = Inicializacao.enderecos[nome]

os.system("title " + nome)

pc = PC(nome, endereco)
pc.pc_conectar(TipoCon.CON_2, Inicializacao.enderecos["PC4"])
pc.pc_conectar(TipoCon.CON_1, Inicializacao.enderecos["PC2"])
pc.pc_conectar(TipoCon.CON_AC, Inicializacao.enderecos["AC"])
print("> > " + nome + " < <")
input("Enter para iniciar")
pc.iniciar()