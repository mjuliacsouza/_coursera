def primo(n):
    i=2
    primo = True

    while i<n:
       if n%i ==0:
           primo = False
           break
       else:
           i = i + 1
    return primo

def maior_primo(n):
    ehprimo=primo(n)
    while ehprimo == False:
        n = n-1
        ehprimo = primo(n)
    return n



