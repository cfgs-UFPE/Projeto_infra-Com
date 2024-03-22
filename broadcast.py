import socket

def broadcast(mensagem, porta, computador):

    while True:
        for _ in range(6):
            socket = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)  # UDP
            socket.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
            socket.bind('', 0)
            sock.sendto(mensagem, (< broadcast >, porta))
            sock.close()