import copy
tailleM = 15
def printMat(Matrice, tailleM):
    for i in range(tailleM):
        print([Matrice[i][j] for j in range(tailleM)])
def TerminalTest(Matrice):
    jou =1
    diags = diagonals(Matrice, tailleM)
    cols = columns(Matrice, tailleM)
    if [jou, jou, jou, jou, jou] in diags or [jou, jou, jou, jou, jou] in cols or [jou, jou, jou, jou, jou] in Matrice:
        return True
    return False
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
   
    Matrice = [[0 for col in range(tailleM)] for row in range(tailleM)]
    for i in range(0,6):
        Matrice[i][i] == 1
    
    printMat(Matrice, tailleM)
    print(TerminalTest(Matrice))
    
Main()