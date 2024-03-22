import socket
import sys, time
import geral

def broadcast(mensagem, enderecos):

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
 
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    
    while True:
        for i in range(6):

            porta = 1234
            
            sock.bind(('127.0.0.1', 4526))
            sock.sendto(mensagem, ('127.0.0.1', porta))
            sock.close()

            print("mensagem enviada!")

            time.sleep(2)

    
mensagem = 'Hello World'

enderecos = geral.enderecos

broadcast(mensagem, enderecos.values())