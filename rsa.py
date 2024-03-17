from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

def gerar_chaves():
    chave = RSA.generate(2048)
    chave_privada = chave.export_key()
    chave_publica = chave.publickey().export_key()
    return chave_privada, chave_publica

def cifrar_mensagem(mensagem, chave_publica):
    chave = RSA.import_key(chave_publica)
    cifra = PKCS1_OAEP.new(chave)
    mensagem_cifrada = cifra.encrypt(mensagem)
    return mensagem_cifrada

def decifrar_mensagem(mensagem_cifrada, chave_privada):
    chave = RSA.import_key(chave_privada)
    cifra = PKCS1_OAEP.new(chave)
    mensagem_decifrada = cifra.decrypt(mensagem_cifrada)
    return mensagem_decifrada