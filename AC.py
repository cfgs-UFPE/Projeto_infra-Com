from autoridade_certificadora import *
import geral
import os

nome = "AC"
endereco = geral.enderecos[nome]

os.system("title " + nome)

ac = AC(nome, endereco)
ac.ac_conectar(TipoCon.CON_1, geral.enderecos["PC1"])
ac.ac_conectar(TipoCon.CON_2, geral.enderecos["PC2"])
ac.ac_conectar(TipoCon.CON_3, geral.enderecos["PC3"])
ac.ac_conectar(TipoCon.CON_4, geral.enderecos["PC4"])
ac.ac_conectar(TipoCon.CON_5, geral.enderecos["PC5"])
ac.ac_conectar(TipoCon.CON_6, geral.enderecos["PC6"])
print("> > " + nome + " < <")
input("Enter para iniciar")
ac.iniciar()