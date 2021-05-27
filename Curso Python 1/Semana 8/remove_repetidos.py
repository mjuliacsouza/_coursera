def remove_repetidos(lista):
    aux=lista[:]
    for i in range(len(lista)-1):
        for j in range(i+1,len(lista)):
            if lista[i]==lista[j]:
                aux[j]="repetido"
    lista_final=[]
    for l in aux:
        if l !="repetido":
            lista_final.append(l)
    lista_final.sort()
    return lista_final

