def sao_multiplicaveis(m1,m2):
    linha1 = len(m1)
    coluna1 = len(m1[0])
    linha2 = len(m2)
    coluna2 = len(m2[0])
    if linha2==coluna1:
        return True
    else:
        return False