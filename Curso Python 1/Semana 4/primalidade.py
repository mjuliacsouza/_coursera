n = int(input("Digite um número inteiro: "))
i=2
primo = True

while i<n:
   if n%i ==0:
       primo = False
       break
   else:
       i = i + 1

if primo:
    print("primo")
else:
    print("não primo")
