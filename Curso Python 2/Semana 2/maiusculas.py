def maiusculas(frase):
    pos = 0
    nova_frase=''
    while pos<len(frase):
        if ord(frase[pos])>=64 and ord(frase[pos])<=90:
            nova_frase = nova_frase + frase[pos]
        pos = pos + 1
    return nova_frase


