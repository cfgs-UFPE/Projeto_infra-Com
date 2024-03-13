from autoridade_certificadora import *
import Inicializacao
import os

nome = "AC"
endereco = Inicializacao.enderecos[nome]

os.system("title " + nome)

ac = AC(nome, endereco)
ac.ac_conectar(TipoCon.CON_1, Inicializacao.enderecos["PC1"])
ac.ac_conectar(TipoCon.CON_2, Inicializacao.enderecos["PC2"])
ac.ac_conectar(TipoCon.CON_3, Inicializacao.enderecos["PC3"])
ac.ac_conectar(TipoCon.CON_4, Inicializacao.enderecos["PC4"])
ac.ac_conectar(TipoCon.CON_5, Inicializacao.enderecos["PC5"])
ac.ac_conectar(TipoCon.CON_6, Inicializacao.enderecos["PC6"])
print("> > " + nome + " < <")
input("Enter para iniciar")
ac.iniciar()