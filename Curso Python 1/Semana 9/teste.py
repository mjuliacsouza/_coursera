

lista_similaridades = [2,3,5,1,4]
maior = lista_similaridades[0]
for i in range(len(lista_similaridades) - 1):
    for j in range(i + 1, len(lista_similaridades)):
        if lista_similaridades[i] < lista_similaridades[j]:
            if lista_similaridades[j] > maior:
                maior = lista_similaridades[j]
                i_maior=j
print(i_maior)