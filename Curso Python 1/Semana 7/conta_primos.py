def primalidade(n):
    i=2
    primo = True
    while i<n:
        if n%i ==0:
            primo = False
            break
        else:
            i = i + 1
    return primo

def n_primos(n):
    cont=0
    while n>1:
        ehprimo=primalidade(n)
        if ehprimo:
            cont=cont+1
        n=n-1
    return cont

