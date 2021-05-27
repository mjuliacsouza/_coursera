def conta_letras(frase, contar="vogais"):
    qtd_v = 0
    qtd_c = 0
    lista_vogais = ['a','e','i','o','u','A','E','I','O','U']
    for letra in frase:
        ehVogal = False
        for vogal in lista_vogais:
            if letra == vogal:
                ehVogal = True
        if ehVogal == True:
            qtd_v += 1
        elif not ehVogal and letra != ' ':
            qtd_c += 1
    if contar == "vogais":
        qtd = qtd_v
    else:
        qtd = qtd_c
    return qtd

