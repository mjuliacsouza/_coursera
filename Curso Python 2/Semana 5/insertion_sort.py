def insertion_sort(lista):
    for i in range(len(lista)):
        maior = lista[i]
        for j in range(i):
            if lista[j]>lista[i]:
                lista[j], lista[i] = lista[i], lista[j]
    return lista
                
