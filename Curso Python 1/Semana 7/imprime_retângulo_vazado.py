largura=int(input("digite a largura: "))
altura=int(input("digite a altura: "))

caltura=altura
while caltura>0:
    clargura=largura
    while clargura>0:
        if caltura==altura or caltura==1:
            print("#",end='')
            clargura=clargura-1
        else:
            if clargura==largura or clargura==1:
                print('#',end='')
            else:
                print(" ",end='')
            clargura=clargura-1
    caltura=caltura-1
    print()
