print('Bem-vindo ao jogo do NIM! Escolha:')
print()
print('1 - para jogar uma partida isolada')
modo_de_jogo=int(input('2 - para jogar um campeonato '))

print()
if modo_de_jogo == 2:
    print("Voce escolheu um campeonato!")
    rodada=1
    while rodada<=3:
        print()
        print(f'**** Rodada {rodada} ****')
        print()
        peças=int(input("Quantas peças? "))
        limite_peças=int(input("Limite de peças por jogada? "))
        print()
        print("Computador começa!")
        print()
        npeças=peças
        vez_comp = True
        while npeças>0:
            while npeças>1:
                if vez_comp:
                    print("O computador tirou uma peça.")
                    npeças = npeças - 1
                    if npeças>1:
                        print(f'Agora restam {npeças} peças no tabuleiro.')
                        print()

                    tirar_valido=False
                    while tirar_valido==False:
                        tirar=int(input("Quantas peças você vai tirar? "))
                        print()
                        if tirar>limite_peças:
                            print("Oops! Jogada inválida! Tente de novo.")
                            print()
                        else:
                            tirar_valido=True
                    vez_comp=False
                else:
                    print("Você tirou uma peça.")
                    npeças = npeças - 1
                    if npeças>1:
                        print(f'Agora restam {npeças} peças no tabuleiro.')
                        print()
                    vez_comp=True
            print("Agora resta apenas uma peça no tabuleiro.")
            print()
            npeças=npeças-1
            if vez_comp:
                print("O computador tirou uma peça.")
                print("Fim do jogo! O computador ganhou!")
            else:
                print("Você tirou uma peça.")
                print("Fim do jogo! Você ganhou!")
        rodada=rodada+1
else:
    print('Voce escolheu uma partida isolada!')

