def solve(n):
    somme=0
    puissance=str(n**1000)
    for indice in range(len(puissance)):
        somme+=int(puissance[indice])
    return somme
    

print(solve(2))