lista=[]
n=int(input("Digite um número: "))
while n !=0:
    lista.insert(0,n)
    n = int(input("Digite um número: "))
print()
for i in lista:
    print(i)