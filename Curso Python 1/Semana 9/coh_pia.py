import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''

    soma_difer_ass=0
    for i in range(0,6):
        soma_difer_ass=soma_difer_ass + abs(as_a[i]-as_b[i])
    S_ab = soma_difer_ass/6

    return S_ab

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''

    soma_tam_pala = 0
    n_palavras = 0
    n_pal_dif =0
    n_pal_uni=0
    n_frases=0
    soma_caract_sent =0
    soma_caract_fras = 0
    lista_sentencas = separa_sentencas(texto)
    n_sentencas = len(lista_sentencas)
    lista_total_palavras=[]
    for sentenca in lista_sentencas:
        lista_frases = separa_frases(sentenca)
        n_frases = n_frases + len(lista_frases)
        soma_caract_sent=soma_caract_sent+len(sentenca)
        for frase in lista_frases:
            lista_palavras = separa_palavras(frase)
            soma_caract_fras = soma_caract_fras + len(frase)
            for palavra in lista_palavras:
                soma_tam_pala=soma_tam_pala+len(palavra)
                n_palavras = n_palavras+1
                lista_total_palavras.append(palavra)
    n_pal_dif = n_palavras_diferentes(lista_total_palavras)
    n_pal_uni = n_palavras_unicas(lista_total_palavras)

    """Tamanho médio das palavras"""
    wal = soma_tam_pala/n_palavras

    """Relação Type-Token"""
    ttr = n_pal_dif/n_palavras

    """Razão Hapax Legomana"""
    hlr = n_pal_uni/n_palavras

    """Tamanho médio de sentença"""
    sal=soma_caract_sent/n_sentencas

    """Complexidade de sentença"""
    sac = n_frases/n_sentencas

    """"Tamanho médio de frase"""
    pal = soma_caract_fras/n_frases

    return [wal,ttr,hlr,sal,sac,pal]

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''

    lista_similaridades =[]
    for texto in textos:
        ass_tx = calcula_assinatura(texto)
        similaridade = compara_assinatura(ass_tx,ass_cp)
        lista_similaridades.append(similaridade)
    menor = lista_similaridades[0]
    ind_menor = 0
    for i in range(len(lista_similaridades) - 1):
        for j in range(i + 1, len(lista_similaridades)):
            if lista_similaridades[i] > lista_similaridades[j]:
                if lista_similaridades[j] < menor:
                    menor = lista_similaridades[j]
                    ind_menor=j
    infectado = ind_menor + 1

    return infectado

def main():
    ass_cp = le_assinatura()
    textos = le_textos()
    infectado = avalia_textos(textos,ass_cp)
    print(f'O autor do texto {infectado} está infectado com COH-PIAH')

main()
