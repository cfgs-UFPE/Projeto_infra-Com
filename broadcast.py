import socket
import sys, time

def broadcast(mensagem, porta, computador):

    socket = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)
    socket.bind('', 0)
    socket.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
    
    while True:
        for _ in range(6):

            sock.sendto(mensagem, (< broadcast >, porta))
            sock.close()

            time.sleep(2)