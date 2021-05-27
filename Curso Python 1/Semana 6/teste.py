def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
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
        cp_ganhou = cp_ganhou + 1
    else:
        print("Fim do jogo! Você computador ganhou!")
        print()
        vc_ganhou = vc_ganhou + 1