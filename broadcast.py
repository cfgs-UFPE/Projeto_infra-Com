import socket

def broadcast(mensagem):
    
    socket = socket(AF_INET, SOCK_DGRAM)
    socket.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)