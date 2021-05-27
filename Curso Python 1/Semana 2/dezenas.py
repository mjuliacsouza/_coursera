inteiro=int(input("Digite um número inteiro: "))

aux = inteiro - (inteiro //100)*100
dezenas = aux//10

print("O dígito das dezenas é",dezenas)