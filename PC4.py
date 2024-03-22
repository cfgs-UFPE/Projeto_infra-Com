from app_conversa import *
from pc import *
import geral
import os

nome = "PC4"
endereco = geral.enderecos[nome]

os.system("title " + nome)

app_conversa = APP(nome, "PC1", "PC2", "PC3", "PC5", "PC6")

pc = PC(nome, endereco, app_conversa)
pc.pc_conectar(TipoCon.CON_2, geral.enderecos["PC5"])
pc.pc_conectar(TipoCon.CON_1, geral.enderecos["PC3"])
pc.pc_conectar(TipoCon.CON_AC, geral.enderecos["AC"])
print("> > " + nome + " < <")
#input("Enter para iniciar")
time.sleep(1)
pc.iniciar()