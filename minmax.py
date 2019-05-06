import copy
import math
prof = 6
#test
tailleM = 15
tour = 1
def Actions(Matrice, tailleM,tour):
    valeur = []
    if(tour >3 or tour == 2):
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
def columns(Matrice, tailleM):
    cols =[]
    col=[]
    for i in range(0,tailleM):
        for j in range(0,tailleM):
            col.append(Matrice[j][i])
        cols.append(copy.deepcopy(col))
        col.clear()
    return cols   
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

def Result(Matrice, i,j,jou):
    Matrice[i][j]=jou
    return Matrice
def Utility(Matrice, tailleM,jou):
    diags = diagonals(Matrice, tailleM)
    cols = columns(Matrice, tailleM)
    points = 0
    for elem in diags:
        count = 0
        for x in elem:
            if(x == jou):
                points +=1
                count +=1
            if(x !=jou):
                points -=1
                count=0
            for i in range(2,4):
                if(count == i):

                    points += 20*i
    for elem in cols:
        
        for x in elem:
            if(x == jou):
                points +=1
                count +=1
            if(x !=jou):
                points -=1
                count=0
            for i in range(2,4):
                if(count == i):

                    points += 20*i
    for elem in Matrice:
        
        for x in elem:
            if(x == jou):
                points +=1
                count +=1
            if(x !=jou):
                points -=1
                count=0
            for i in range(2,4):
                if(count == i):

                    points += 20*i
    if(TerminalTest(Matrice)==True):
        points += 80
    
    
    return points

def vainqueur(Matrice, joueur):
    win_Matrice = [
        [Matrice[0][0], Matrice[0][1], Matrice[0][2]],
        [Matrice[1][0], Matrice[1][1], Matrice[1][2]],
        [Matrice[2][0], Matrice[2][1], Matrice[2][2]],
        [Matrice[0][0], Matrice[1][0], Matrice[2][0]],
        [Matrice[0][1], Matrice[1][1], Matrice[2][1]],
        [Matrice[0][2], Matrice[1][2], Matrice[2][2]],
        [Matrice[0][0], Matrice[1][1], Matrice[2][2]],
        [Matrice[2][0], Matrice[1][1], Matrice[0][2]],
    ]
    
    if [joueur, joueur, joueur] in win_Matrice:
        return True
    if Actions(Matrice,tailleM,tour) == []:
        return True
    else:
        return False

def TerminalTest(Matrice):
    diags = diagonals(Matrice, tailleM)
    cols = columns(Matrice, tailleM)
    for jou in [1,2]:
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
        for elem in Matrice:
            count = 0
            for x in elem:
                if(x == jou):
                    count +=1
                if(x !=jou):
                    count =0
                if(count == 5):
                    return True
    return False
def MaxValue(Matrice, tailleM,jou,p, profondeur, Alpha, Beta,tour):
    if(TerminalTest(Matrice) or profondeur == prof):
        return Utility(Matrice, tailleM,jou[p])
    res = Actions(Matrice, tailleM,tour)
    best = []
    
    for x in res:
        
        mm= MinValue(Result(copy.deepcopy(Matrice), x[0],x[1],jou[p]),tailleM,jou,(p+1)%2,profondeur+1, Alpha, Beta,copy.deepcopy(tour+1))
        if(mm > Beta):
            return mm
        
        best.append(mm)
    
    best = sorted(best,reverse=True)
    best = best[0]
    Alpha = best
    return best
def MinValue(Matrice, tailleM, jou,p, profondeur, Alpha, Beta, tour):
    if(TerminalTest(Matrice) or profondeur == prof ):
        return Utility(Matrice, tailleM,jou[p])
    res = Actions(Matrice, tailleM,tour)
    
    best = []
    
    for x in res:
       
        mm = MaxValue(Result(copy.deepcopy(Matrice), x[0],x[1],jou[p]),tailleM,jou,(p+1)%2,profondeur+1, Alpha, Beta,copy.deepcopy(tour+1))
        if(mm < Alpha):
            return mm
        best.append(mm)
    
    best = sorted(best)
    best = best[0]
    Beta = best
    return best
def takefirst(elem):
    return elem[0]
def MiniMaxDecision(Matrice, tailleM,var, profondeur,tour):
    res = Actions(Matrice, tailleM,tour)    
    point =[]
    jou=[1,2]
    p=var
    
    for x in res:        
        
        mm = MinValue(Result(copy.deepcopy(Matrice), x[0],x[1],jou[p]),tailleM,jou,(p+1)%2, profondeur,math.inf,-math.inf,copy.deepcopy(tour+1))
        
        point.append([mm,x[0],x[1]])
    
    point = sorted(point, key=lambda l:l[0], reverse = True)
    print("POSSSIBILITES : ")
    print(point)
    return point[0]
def Main():
    
    Matrice = [[0 for col in range(tailleM)] for row in range(tailleM)]
    result = False
    tour = 1
    while result==False:   
        
        temp = MiniMaxDecision(copy.deepcopy(Matrice), tailleM,0,0,copy.deepcopy(tour))
        Matrice = Result(Matrice,temp[1],temp[2],1)
        printMat(Matrice, tailleM)
        result = TerminalTest(Matrice)
        userinput(Matrice, tailleM)
        printMat(Matrice, tailleM)
        result = TerminalTest(Matrice)
        tour +=1
    
    printMat(Matrice, tailleM)       
def userinput(Matrice,tailleM):
    x = input("Coordonées X de votre choix ?")
    y = input("Coordonées Y de votre choix ?")
    while(Matrice[int(x)][int(y)]!=0):
        print("CASE DEJA PRISE ")
        printMat(Matrice, tailleM)
        x = input("Coordonées X de votre choix ?")
        y = input("Coordonées Y de votre choix ?")
    Result(Matrice,int(x),int(y),2)
def printMat(Matrice, tailleM):
    for i in range(tailleM):
        print([Matrice[i][j] for j in range(tailleM)])

Main()
