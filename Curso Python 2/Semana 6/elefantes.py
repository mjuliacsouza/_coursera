def incomodam(n):
    frase = ''
    if n>0 and n%1 == 0:
        frase = 'incomodam '+incomodam(n-1)
        return frase
    return frase

def elefantes(n):
    if n == 1:        
        return "Um elefante incomoda muita gente\n" 
    elif n == 2:
        return "Um elefante incomoda muita gente\n" + "{} elefantes {}muito mais\n".format(n,incomodam(n))
    elif not (n>0 and n%1 == 0):
        return ''
    else:
        return  elefantes(n-1) + "{} elefantes incomodam muita gente\n".format(n-1,incomodam(n-1)) + "{} elefantes {}muito mais\n".format(n,incomodam(n))






  
    
