from app_conversa import *
from pc import *
import geral
import os

nome = "PC6"
endereco = geral.enderecos[nome]

os.system("title " + nome)

app_conversa = APP(nome, "PC1", "PC2", "PC3", "PC4", "PC5")

pc = PC(nome, endereco, app_conversa)
pc.pc_conectar(TipoCon.CON_2, geral.enderecos["PC1"])
pc.pc_conectar(TipoCon.CON_1, geral.enderecos["PC5"])
pc.pc_conectar(TipoCon.CON_AC, geral.enderecos["AC"])
print("> > " + nome + " < <")
#input("Enter para iniciar")
time.sleep(1)
pc.iniciar()