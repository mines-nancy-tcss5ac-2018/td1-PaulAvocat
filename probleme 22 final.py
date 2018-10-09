fichier=open('C:/Users/tuto/Documents/pyhthon ficm/p022_names.txt', 'r')
L=[]
for e in fichier:
    L.append(e)
fichier.close

##
def divisionliste(liste): #fonction remplace split car nous n'étions pas prévenus 
    listedivisee=[]
    longueur=len(liste[0])
    indice1=0
    for indice2 in range(longueur):
        if liste[0][indice2]==',':
            listedivisee.append(liste[0][indice1+1:indice2-1])
            indice1=indice2+1
    listedivisee.append(liste[0][longueur-7:longueur-1])
    return listedivisee 
    
def tri(liste):
    liste_divisee=divisionliste(liste)
    liste_triee=sorted(liste_divisee)
    return(liste_triee)
    
print(tri(L)) #donne une liste avec les prénoms séparés

## SOMME

Valeurs={'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}

prenoms=tri(L)

def  somme(liste):
    liste_score=[]
    for prenom in liste:
        score=0
        longueur=len(prenom)
        for indice in range(longueur):
            score+=Valeurs[prenom[indice]]
        liste_score.append(score)
    return liste_score
    
print(somme(prenoms))

## SCORE TOTAL

def score_total(liste):
    scoretot=0
    liste_somme=somme(prenoms)
    longueur=len(liste_somme)
    for indice in range(longueur):
        scoretot+=(indice+1)*liste_somme[indice]
    return scoretot
    
print(score_total(L))

