"""
n=numero de peças
m=limite de peças
"""
def quem_começa (n,m):
   if n%(m+1)==0:
       cp_começa=False
   else:
       cp_começa=True
   return cp_começa


def computador_escolhe_jogada (n,m):
   if n%(m+1)<m:
       jogada = n%(m+1)
   else:
       if n>m:
           jogada=m
       else:
           jogada=n
   return jogada

def usuario_escolhe_jogada (n,m):
    tirar_valido=False
    while not tirar_valido:
        tirar = int(input("Quantas peças você vai tirar? "))
        if tirar>m or tirar<=0:
            print()
            print("Oops! Jogada inválida! Tente de novo.")
            print()
        else:
            tirar_valido=True
    return tirar

def partida():
    n_valido=False
    while not n_valido:
        n = int(input("Quantas peças? "))
        if n<=0:
            print()
            print("Oops! Jogada inválida! Tente de novo.")
            print()
        else:
            n_valido=True
    m_valido = False
    while not m_valido:
        m = int(input("Limite de peças por jogada? "))
        if m <= 0 or m>n:
            print()
            print("Oops! Jogada inválida! Tente de novo.")
            print()
        else:
            m_valido = True
    print()
    vez_cp = quem_começa(n, m)
    if vez_cp:
        print("Computador começa!")
        print()
    else:
        print("Você começa!")
        print()
    partida = True
    while partida:
        if vez_cp:
            jogada_c = computador_escolhe_jogada(n, m)
            n = n - jogada_c
            if jogada_c == 1:
                print(f'O computador tirou uma peça.')
            else:
                print(f'O computador tirou {jogada_c} peças.')
            vez_cp = False
        else:
            jogada_u = usuario_escolhe_jogada(n, m)
            n = n - jogada_u
            if jogada_u == 1:
                print(f'Você tirou uma peça.')
            else:
                print(f'Você tirou {jogada_u} peças.')
            vez_cp = True
        if n > 1:
            print(f"Agora restam {n} peças no tabuleiro.")
            print()
        elif n == 1:
            print("Agora resta apenas uma peça no tabuleiro.")
            print()
        elif n == 0:
            partida = False
    if vez_cp == False:
        print("Fim do jogo! O computador ganhou!")
        print()
    else:
        print("Fim do jogo! Você computador ganhou!")
        print()
    return vez_cp

def campeonato():
    print("Voce escolheu um campeonato!")
    rodada = 1
    vc = 0
    cp = 0
    while rodada <= 3:
        print(f'**** Rodada {rodada} ****')
        print()
        vc_ganhou=partida()
        if vc_ganhou:
            vc= vc+1
        else:
            cp=cp+1
        rodada = rodada + 1
    return (vc,cp)


def jogo_nim():
    print('Bem-vindo ao jogo do NIM! Escolha:')
    print()
    print('1 - para jogar uma partida isolada')
    modo_de_jogo = int(input('2 - para jogar um campeonato '))
    print()

    if modo_de_jogo == 2:
        resultado=campeonato()
        print("**** Final do campeonato! ****")
        print()
        print(f"Placar: Você {resultado[0]} X {resultado[1]} Computador")
    else:
        partida()


jogo_nim()
