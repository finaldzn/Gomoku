import copy
def printMat(Matrice, tailleM):
    for i in range(tailleM):
        print([Matrice[i][j] for j in range(tailleM)])
def diagonals(Matrice, tailleM):
    diags =[]
    diag = []
    for i in range(0,tailleM):
        diag.append(Matrice[i][i])
    diags.append(copy.deepcopy(diag))
    diag.clear()
    j= 0
    for i in range(tailleM-1,-1,-1):
        diag.append(Matrice[i][j])
        j +=1
    diags.append(copy.deepcopy(diag))
    for offset in range(tailleM):
        diag = [ row[i+offset] for i,row in enumerate(Matrice) if 0 <= i+offset < len(row)]
        diags.append(copy.deepcopy(diag))
        diag.clear()
    diag.clear()

    return diags
def Main():
    tailleM = 15
    Matrice = [[0 for col in range(tailleM)] for row in range(tailleM)]
    
    Matrice[0][10]= 1
    Matrice[1][7]= 1
    printMat(Matrice, tailleM)
    print(diagonals(Matrice,tailleM))
    
Main()