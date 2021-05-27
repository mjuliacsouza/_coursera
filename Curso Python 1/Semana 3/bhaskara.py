a=float(input())
b=float(input())
c=float(input())

delta = b**2 - 4*a*c

if delta == 0:
    x = -b/(2*a)
    print("a raiz desta equação é",x)
elif delta <0:
    print("esta equação não possui raízes reais")
elif delta >0:
    x1 = (-b + ((delta) ** (1 / 2))) / (2 * a)
    x2 = (-b - ((delta) ** (1 / 2))) / (2 * a)
    if x1>x2:
        print("as raízes da equação são",x2,"e",x1)
    else:
        print("as raízes da equação são", x1, "e", x2)