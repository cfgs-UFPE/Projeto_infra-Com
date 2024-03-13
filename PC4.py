from pc import *
import Inicializacao
import os

nome = "PC4"
endereco = Inicializacao.enderecos[nome]

os.system("title " + nome)

pc = PC(nome, endereco)
pc.pc_conectar(TipoCon.CON_2, Inicializacao.enderecos["PC5"])
pc.pc_conectar(TipoCon.CON_1, Inicializacao.enderecos["PC3"])
pc.pc_conectar(TipoCon.CON_AC, Inicializacao.enderecos["AC"])
print("> > " + nome + " < <")
input("Enter para iniciar")
pc.iniciar()