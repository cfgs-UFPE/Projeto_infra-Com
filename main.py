from pc import *
from autoridade_certificadora import *

pc1 = PC("PC1", 1234)
pc2 = PC("PC2", 5678)
pc3 = PC("PC3", 4321)
pc4 = PC("PC4", 8765)
pc5 = PC("PC5", 9101)
pc6 = PC("PC6", 1121)
conectar_pc_pc(pc1, pc2)
conectar_pc_pc(pc2, pc3)
conectar_pc_pc(pc3, pc4)
conectar_pc_pc(pc4, pc5)
conectar_pc_pc(pc5, pc6)
conectar_pc_pc(pc6, pc1)
print("ok")