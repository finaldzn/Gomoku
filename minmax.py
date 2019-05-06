import copy
import math
prof = 6
tailleM = 3
def Actions(Matrice, tailleM):
    valeur = []
    for i in range(tailleM):
        for j in range(tailleM):
            if Matrice[i][j]==0:
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
    diag.clear()

    return diags

def Result(Matrice, i,j,jou):
    Matrice[i][j]=jou
    return Matrice
def Utility(Matrice, tailleM,jou):
    
    points = 0
    for i in range(tailleM):
        if columns(Matrice, tailleM)[i].count(jou) == 2:
            points +=10
        if diagonals(Matrice, tailleM)[i%2].count(jou) == 2:
            points +=10
        for j in range(tailleM):
            #ligne(droite vers gauche)
            for y1 in range(j, 0,-1):
                    if(Matrice[i][y1]==jou):
                        points+=1
                    if(Matrice[i][y1]!=jou & Matrice[i][y1]!=0):
                        points-=2
                    if(Matrice[i][y1]==0):
                        points+=1
            
            #colonne(bas vers haut)
            for x1 in range(i, 0,-1):
                    if(Matrice[x1][j]==jou):
                        points+=1
                    if(Matrice[x1][j]!=jou & Matrice[x1][j]!=0):
                        points-=2
                    if(Matrice[x1][j]==0):
                        points+=1
            #ligne (gauche vers droite)
            for y1 in range(j, tailleM):
                if(Matrice[i][y1]==jou):
                    points+=1
                if(Matrice[i][y1]!=jou & Matrice[i][y1]!=0):
                    points-=2
                if(Matrice[i][y1]==0):
                    points+=1
            #colonne(haut vers bas)
            for x1 in range(i, tailleM):
                if(Matrice[x1][j]==jou):
                    points +=1
                if(Matrice[x1][j]!=jou & Matrice[x1][j]!=0):
                    points-=2
                if(Matrice[x1][j]==0):
                        points+=1
            #diagonale(gauche vers droite)
            if(i !=2 or j!=2):
                for x in range(i,tailleM):
                    for y in range(tailleM):
                        if(j+y <tailleM):
                            if(Matrice[x][j+y]==jou):
                                points +=1
                            if(Matrice[x][j+y]!=jou & Matrice[x][j+y]!=0):
                                points-=2
                            if(Matrice[x][j+y]==0):
                                points+=1
            #diagonale(droite vers gauche)
            if(i !=2 or j!=2):
                for y in range(j,0,-1):
                    for x in range(tailleM):
                        if(i-x >0):
                            if(Matrice[i-x][y]==jou):
                                points +=1
                            if(Matrice[i-x][y]!=jou & Matrice[i-x][y]!=0):
                                points-=2
                            if(Matrice[i-x][y]==0):
                                points+=1
    if(vainqueur(Matrice, jou)==True):
        points += 80
    
    if(vainqueur(Matrice,jou)==False):
        points -= 30
    
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
    if Actions(Matrice,tailleM) == []:
        return True
    else:
        return False
def TerminalTest(Matrice):
    return vainqueur(Matrice, 1) or vainqueur(Matrice, 2)
def test(Matrice, tailleM):
    
    diags = diagonals(Matrice, tailleM)
    cols = columns(Matrice, tailleM)
    win = 0
    count = 0
    count2 =0
    for jou in range(1,tailleM):
        var = [jou for elem in range(tailleM)]
        
        for i in range(tailleM):
            if Matrice[i].count(jou)==tailleM:
                win = jou
                break
            if Matrice[i].count(jou)==tailleM-1 and Matrice[i].count(0)==0:
                count +=1
                if count ==tailleM:
                    win =3
                    break
            if cols[i].count(jou)==tailleM-1 and cols[i].count(0)==0:
                count2 +=1
                if count2 ==3:
                    win =3
                    break     
        if  var in diags or var in cols or var in Matrice:
            win = jou
            break
        

    return win


def MaxValue(Matrice, tailleM,jou,p, profondeur, Alpha, Beta):
    if(TerminalTest(Matrice) or profondeur == prof):
        return Utility(Matrice, tailleM,jou[p])
    res = Actions(Matrice, tailleM)
    best = []
    
    for x in res:
        
        mm= MinValue(Result(copy.deepcopy(Matrice), x[0],x[1],jou[p]),tailleM,jou,(p+1)%2,profondeur+1, Alpha, Beta)
        if(mm > Beta):
            return mm
        
        best.append(mm)
    
    best = sorted(best,reverse=True)
    best = best[0]
    Alpha = best
    return best


def MinValue(Matrice, tailleM, jou,p, profondeur, Alpha, Beta):
    if(TerminalTest(Matrice) or profondeur == prof ):
        return Utility(Matrice, tailleM,jou[p])
    res = Actions(Matrice, tailleM)
    
    best = []
    
    for x in res:
       
        mm = MaxValue(Result(copy.deepcopy(Matrice), x[0],x[1],jou[p]),tailleM,jou,(p+1)%2,profondeur+1, Alpha, Beta)
        if(mm < Alpha):
            return mm
        best.append(mm)
    
    best = sorted(best)
    best = best[0]
    Beta = best
    return best
def takefirst(elem):
    return elem[0]

def MiniMaxDecision(Matrice, tailleM,var, profondeur):
    res = Actions(Matrice, tailleM)    
    point =[]
    jou=[1,2]
    p=var
    
    for x in res:        
        
        mm = MinValue(Result(copy.deepcopy(Matrice), x[0],x[1],jou[p]),tailleM,jou,(p+1)%2, profondeur,math.inf,-math.inf)
        
        point.append([mm,x[0],x[1]])
    
    point = sorted(point, key=lambda l:l[0], reverse = True)
    print("POSSSIBILITES : ")
    print(point)
    return point[0]

def Main():
    
    Matrice = [[0 for col in range(tailleM)] for row in range(tailleM)]
    result = False
    
    while result==False:   
        
        temp = MiniMaxDecision(copy.deepcopy(Matrice), tailleM,0,0)
        Matrice = Result(Matrice,temp[1],temp[2],1)
        printMat(Matrice, tailleM)
        result = TerminalTest(Matrice)
        userinput(Matrice, tailleM)
        printMat(Matrice, tailleM)
        result = TerminalTest(Matrice)
    if vainqueur(Matrice,1): win =1
    if vainqueur(Matrice,2): win =2
    print(win)   
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
