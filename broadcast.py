import socket
import sys, time
import geral

def broadcast(mensagem, enderecos):

    socket = socket(AF_INET, SOCK_DGRAM)
 
    socket.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
    
    while True:
        for i in range(len(enderecos.keys())):

            porta = enderecos[i][1]
            
            socket.bind(enderecos[i][0], porta)
            sock.sendto(mensagem, (< broadcast >, porta))
            sock.close()

            time.sleep(2)