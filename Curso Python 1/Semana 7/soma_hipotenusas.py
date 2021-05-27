def é_hipotenusa(a, b):
    hipotenusa = ((a * a) + (b * b))
    return hipotenusa

def soma_hipotenusas(n):
    c = 1
    soma = 0
    while (c <= n):
        c2 = (c * c)
        a = 1
        b = 1
        while (a < n):
            while (b < n):
                if (c2 == é_hipotenusa(a, b)):  # Chamada da função que calcula hipotenusa
                    # print(a, " - " ,b , " - " , c)
                    soma = soma + c
                    a = n
                    break
                b += 1
            a += 1
            b = a
        c += 1
    return soma

