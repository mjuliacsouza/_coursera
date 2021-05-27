def maior_elemento(lista):
    maior=lista[0]
    for i in range(len(lista)-1):
        for j in range(i+1,len(lista)):
            if lista[i]<lista[j] :
                if lista[j]>maior:
                    maior = lista[j]
    return maior

lista=[3,2,5,4,1]
print(maior_elemento(lista))
