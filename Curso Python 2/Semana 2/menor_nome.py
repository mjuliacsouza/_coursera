def menor_nome(lista_de_nomes):
    nova_lista=[]
    for nome in lista_de_nomes:
        nome = nome.strip()
        nome = nome.capitalize()
        nova_lista.append(nome)
    menor = nova_lista[0]
    for nome in nova_lista:
        if len(nome)<len(menor):
            menor = nome
    return menor


