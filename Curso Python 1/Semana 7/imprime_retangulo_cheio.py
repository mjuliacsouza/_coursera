largura=int(input("digite a largura: "))
altura=int(input("digite a altura: "))

while altura>0:
    cont=largura
    while cont>0:
        print("#", end='')
        cont=cont-1
    altura=altura-1
    print()

