import rsa 
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes as random
import base64

"""
O objetivo das funções encriptar_chave_privada e decriptar_chave_privada é não enviar a chave privada para o computador em plaintext. 
"""

def encriptar_chave_privada(chave_privada):
    
    chave = random(16)

    encriptador = AES.new(chave, AES.MODE_EAX, nonce = nonce)

    chave_privada_encriptada = encriptador.encrypt(chave_privada)

    return chave

def decriptar_chave_privada(chave_privada_encriptada):

    chave = random(16)

    decriptador = AES.new(chave, AES.MODE_EAX, nonce = nonce)

    message = decriptador.decrypt(chave_privada_encriptada)

    return message

def decriptar(cifra_b64str, chave_privada):

    #chave_privada = decriptar_chave_privada(chave_privada_encriptada)

    cifra = base64.b64decode(cifra_b64str)

    mensagem_byte = rsa.decrypt(cifra, chave_privada) # aqui o código decripta a cifra usando a chave privada do computador

    mensagem = mensagem_byte.decode()

    return mensagem

def encriptar(mensagem, chave_publica):
    
    mensagem_encoded = mensagem.encode()

    cifra = rsa.encrypt(mensagem_encoded, chave_publica) # aqui o código encripta a mengagem usando a chave pública.

    cifra_str = base64.b64encode(cifra).decode()

    '''x = base64.b64encode(cifra)
    y = x.decode()
    z = base64.b64decode(y)
    
    decriptar(z, p)'''

    return cifra_str