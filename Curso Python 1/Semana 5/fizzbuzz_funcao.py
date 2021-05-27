def fizz(n):
    if n%3==0:
        ehfizz=True
    else:
        ehfizz=False
    return ehfizz

def buzz(n):
    if n%5==0:
        ehbuzz=True
    else:
        ehbuzz=False
    return ehbuzz

def fizzbuzz(n):
    ehbuzz=buzz(n)
    ehfizz=fizz(n)
    if ehbuzz and ehfizz:
        return ("FizzBuzz")
    elif ehbuzz and not ehfizz:
        return("Buzz")
    elif ehfizz and not ehbuzz:
        return ("Fizz")
    else:
        return n
