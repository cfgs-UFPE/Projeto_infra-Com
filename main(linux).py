import subprocess

# Lista de comandos a serem executados em cada terminal
comandos = [
    "python3 AC.py",
    "python3 PC1.py",
    "python3 PC2.py",
    "python3 PC3.py",
    "python3 PC4.py", 
    "python3 PC5.py",
    "python3 PC6.py"
]

# Função para abrir um terminal e executar um comando nele
def abrir_terminal_e_executar_comando(comando):
    terminal_command = f"gnome-terminal -- bash -c '{comando}; exec bash'"
    subprocess.Popen(terminal_command, shell=True)

# Executar os comandos em terminais separados
for prompt_c in comandos:
    abrir_terminal_e_executar_comando(prompt_c)