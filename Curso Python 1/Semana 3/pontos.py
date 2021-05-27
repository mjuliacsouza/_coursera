coordX1 = int(input())
coordY1 = int(input())
coordX2 = int(input())
coordY2 = int(input())

distancia = (((coordX1-coordX2)**2)+((coordY1-coordY2)**2))**(1/2)

if (distancia>=10):
    print("longe")
else:
    print("perto")