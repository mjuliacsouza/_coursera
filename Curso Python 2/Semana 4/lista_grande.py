import random

def  lista_grande(n):
    lista=[]
    for i in range(n):
        aleat = int(random.random()*10)
        lista.append(aleat)
    return lista
