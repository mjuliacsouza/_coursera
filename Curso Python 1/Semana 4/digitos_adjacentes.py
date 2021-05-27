n = int(input("Digite um número inteiro: "))

if n ==0:
    adj = False
else:
    ultimo=n%10
    n = n//10
    proximo = n%10
    adj = False
    while adj==False:
        if proximo == ultimo:
            adj = True
            break
        elif n==0:
            break
        else:
            ultimo = proximo
            n = n // 10
            proximo = n % 10

if adj == True:
    print("sim")
else:
    print('não')
