import rsa 
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes as random

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

def decriptar(cifra, chave_privada_encriptada):

    chave_privada = decriptar_chave_privada(chave_privada_encriptada)

    mensagem = rsa.decrypt(cifra, chave_privada) # aqui o código decripta a cifra usando a chave privada do computador

    return mensagem

def encriptar(mensagem, remetente, dest):
   
    chave_publica = chaves_dict[dest] # aqui o remetente pega a chave pública do destinatário.

    if chave_publica == NULL: # caso o pc ainda não tenha sido registrado na autoridade certificadora.
        raise OSError('não há registro')

    cifra = rsa.encrypt(mensagem, chave_publica) # aqui o código encripta a mengagem usando a chave pública.

    return cifra 
