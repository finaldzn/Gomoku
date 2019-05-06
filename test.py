
def printMat(Matrice, tailleM):
    for i in range(tailleM):
        print([Matrice[i][j] for j in range(tailleM)])
def Actions(Matrice, tailleM,tour):
    valeur = []
    if(tour >3):
        for i in range(tailleM):
            for j in range(tailleM):
                if Matrice[i][j]==0:
                    valeur.append([i,j])
    if(tour == 1):
        valeur.append([7,7])
    if(tour == 3):
        for i in range(tailleM):
            for j in range(tailleM):
                if Matrice[i][j]==0 and ((i   in [ e for e in range(3,10)] or j  in [e for e in range(3,10)] )== False):
                    valeur.append([i,j])
    return valeur
def Main():
    tailleM = 15
    Matrice = [[0 for col in range(tailleM)] for row in range(tailleM)]
    printMat(Matrice, tailleM)
    print(Actions(Matrice,tailleM,1))
    print(Actions(Matrice,tailleM,2))
    print(Actions(Matrice,tailleM,3))
    print(Actions(Matrice,tailleM,4))
Main()