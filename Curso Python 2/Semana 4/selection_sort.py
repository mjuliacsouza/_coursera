def ordena(lista):
    for j in range(len(lista)-1):
        for i in range(j+1,len(lista)):
            if lista[i]<lista[j]:
                lista[i],lista[j] = lista[j], lista[i]
    return lista
            
        
