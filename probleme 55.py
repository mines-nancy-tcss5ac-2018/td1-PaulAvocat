## Test palindrome

def palindrome(nombre):
    nombre=str(nombre)
    longueur=len(nombre)
    for i in range(0,int(longueur/2)):
        if nombre[i]!=nombre[-1-i]: 
            return (False)
    return (True)
    
##Inversion

def inversion(nombre):
    nombre=str(nombre)
    nombre=nombre[::-1]
    return(int(nombre))
    
##
def compteur_lychrel(n):
    compteur=0
    for x in range(1,n+1):
        nombre=x+inversion(x)
        iteration=0
        while iteration<51 and palindrome(nombre)==False:
            iteration+=1
            nombre+=inversion(nombre)
        if palindrome(nombre)==False:  
            compteur+=1
    return(compteur)
    
print(compteur_lychrel(10000))