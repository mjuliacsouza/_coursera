inteiro = int(input("Digite um número inteiro: "))
soma = 0

while inteiro !=0:
    soma=soma+(inteiro%10)
    inteiro = inteiro // 10
print(soma)
