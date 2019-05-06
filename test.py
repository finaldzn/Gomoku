import copy
tailleM = 15
def printMat(Matrice, tailleM):
    for i in range(tailleM):
        print([Matrice[i][j] for j in range(tailleM)])
def TerminalTest(Matrice, jou):
    
    diags = diagonals(Matrice, tailleM)
    cols = columns(Matrice, tailleM)
    for elem in diags:
        count = 0
        for x in elem:
            if(x == jou):
                count +=1
            if(x !=jou):
                count =0
            if(count == 5):
                return True
    for elem in cols:
        count = 0
        for x in elem:
            if(x == jou):
                count +=1
            if(x !=jou):
                count =0
            if(count == 5):
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
def columns(Matrice, tailleM):
    cols =[]
    col=[]
    for i in range(0,tailleM):
        for j in range(0,tailleM):
            col.append(Matrice[j][i])
        cols.append(copy.deepcopy(col))
        col.clear()
    return cols   
def Main():
   
    Matrice = [[0 for col in range(tailleM)] for row in range(tailleM)]
    for i in range(0,5):
        Matrice[i][i] = 1
    
    printMat(Matrice, tailleM)
    print(TerminalTest(Matrice))
    
Main()