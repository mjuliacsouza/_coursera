def soma_matrizes(m1,m2):
    linha1 = len(m1)
    coluna1 = len(m1[0])
    linha2 = len(m2)
    coluna2 = len(m2[0])

    soma = []

    if linha1==linha2 and coluna1==coluna2:
        for i in range(linha1):
            linha_soma = []
            for j in range(coluna1):
                elemento_soma = m1[i][j] + m2[i][j]
                linha_soma.append(elemento_soma)
            soma.append(linha_soma)
        return soma
    else:
        return False
