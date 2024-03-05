from pc import *
from autoridade_certificadora import *

# Cria tudo:
pc1 = PC("PC1", 1234)
pc2 = PC("PC2", 5678)
pc3 = PC("PC3", 4321)
pc4 = PC("PC4", 8765)
pc5 = PC("PC5", 9101)
pc6 = PC("PC6", 1121)
ac  = AC("AC", 3141)
# Conecta tudo:
conectar_pc_pc(pc1, pc2)
conectar_pc_pc(pc2, pc3)
conectar_pc_pc(pc3, pc4)
conectar_pc_pc(pc4, pc5)
conectar_pc_pc(pc5, pc6)
conectar_pc_pc(pc6, pc1)
conectar_PC_AC(pc1, ac, 1)
conectar_PC_AC(pc2, ac, 2)
conectar_PC_AC(pc3, ac, 3)
conectar_PC_AC(pc4, ac, 4)
conectar_PC_AC(pc5, ac, 5)
conectar_PC_AC(pc6, ac, 6)
# Iniciar Tudo:
pc1.iniciar()
#pc2.iniciar()
#pc3.iniciar()
#pc4.iniciar()
#pc5.iniciar()
#pc6.iniciar()
ac.iniciar()
print("ok")