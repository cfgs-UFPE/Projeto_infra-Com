import rsa 

def decriptar(cifra, chave_privada_encriptada):
    pass
    chave_privada = chave_privada_encriptada
    mensagem = rsa.decrypt(cifra, chave_privada) # aqui o código decripta a cifra usando a chave privada do computador
    return mensagem

def encriptar(mensagem, remetente, dest):
    pass
    chave_publica = chaves_dict[dest] # aqui o remetente pega a chave pública do destinatário.
    cifra = rsa.encrypt(mensagem, chave_publica) # aqui o código encripta a mengagem usando a chave pública.
    return cifra 

