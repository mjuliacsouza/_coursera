def  primeiro_lex(lista):
    primeiro = lista[0]
    for palavra in lista:
        if palavra < primeiro:
            primeiro = palavra
    return primeiro

