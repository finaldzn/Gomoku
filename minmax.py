import copy
import math
prof = 6
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
            col.append([Matrice[j][i],j,i])
        cols.append(copy.deepcopy(col))
        col.clear()
    return cols   
def diagonals(Matrice, tailleM):
    diags =[]
    diag = []
    for i in range(0,tailleM):
        diag.append([Matrice[i][i],i,i])
    diags.append(copy.deepcopy(diag))
    diag.clear()
    j= 0
    for i in range(tailleM-1,-1,-1):
        diag.append([Matrice[i][j],i,j])
        j +=1
    diags.append(copy.deepcopy(diag))
    for offset in range(tailleM):
        diag = [ [row[i+offset],i,i+offset] for i,row in enumerate(Matrice) if 0 <= i+offset < len(row)]
        diags.append(copy.deepcopy(diag))
        diag.clear()
    diag.clear()

    return diags
def ThreatSearch(Matrice, tailleM, jou):
    diags = diagonals(Matrice, tailleM)
    cols = columns(Matrice, tailleM)
    for i in range(tailleM):
        count = 0
        for j in range(tailleM):
            if Matrice[i][j] == jou:                    
                count +=1
            if Matrice[i][j] !=jou:
                if(count == 4):                        
                   return [1000000000,i,j]
                if(count == 3):                        
                   return [1000000,i,j]
                count = 0
    for elem in diags:
        count=0
        for x in elem:
            
            if x[0] == jou:                    
                count +=1
            if x[0] !=jou:
                if(count == 4):                        
                   return [1000000000,x[1],x[2]]
                if(count == 3):                        
                   return [1000000,i,j]
                count=0
    for elem in cols:
        for x in elem:
            count=0
            if x[0] == jou:                    
                count +=1
            if x[0] !=jou:
                if(count == 4):                        
                   return [1000000000,x[1],x[2]]
                if(count == 3):                        
                   return [1000000,i,j]
                count=0

    
    return [-9999999,-1,-1]
def Result(Matrice, i,j,jou):
    Matrice[i][j]=jou
    return Matrice
"""def Utility(Matrice, tailleM,jou):
   
    diags = diagonals(Matrice, tailleM)
    cols = columns(Matrice, tailleM)
    point = 0
    points = 0
    for elem in diags:
        count = 0
       
        for x in elem:
            if(x[0] == jou):                
                count +=1

            if(x[0] !=jou and x[0] !=0):
                if count ==2:
                    points= 100
                if count ==3:
                    points= 1000
                if count ==4:
                    points= 10000000
                if count ==5:
                    points= 1000000000
                count=0
                
            if(x[0] !=jou and x[0] ==0):
                if count ==2:
                    points= 1000
                if count ==3:
                    points= 10000
                if count ==4:
                    points= 10000000
                if count ==5:
                    points= 1000000000                
                count=0
    point = points
    for elem in cols:
        count = 0
        
        for x in elem:
            if(x[0] == jou):                
                count +=1
                
            
            if(x[0] !=jou and x[0] !=0):
                if count ==2:
                    points= 100
                if count ==3:
                    points= 1000
                if count ==4:
                    points= 10000000
                if count ==5:
                    points= 1000000000
                count=0
                
            if(x[0] !=jou and x[0] ==0):
                if count ==2:
                    points=1000
                if count ==3:
                    points= 10000
                if count ==4:
                    points= 10000000
                if count ==5:
                    points=1000000000               
                
                count=0
    point = point + points        
    for elem in Matrice:
        count = 0
        count2 = 0
        for x in elem:
            if(x == jou):                
                count +=1
               
            
            if(x !=jou and x !=0):
                if count ==2:
                    points= 100
                if count ==3:
                    points= 1000
                if count ==4:
                    points= 10000
                if count ==5:
                    points= 100000
                count=0
                count2 +=1
            if(x !=jou  and x ==0):
                if count ==2:
                    points=1000
                if count ==3:
                    points= 10000
                if count ==4:
                    points= 100000
                if count ==5:
                    points=1000000
                
                count=0
                
    point = point + points              
    if(TerminalTest(Matrice)==True):
        point+= 100000 
    
    
    return point
"""
def Utility(Matrice, tailleM,jou,ligne,colonne):
    points = 0
    index = -4
    while(index <= 0):
        adversaire = False
        coequipier = 0
        for i in range((colonne+index),(colonne+index+5)):
            if((colonne+index)>=0 and (colonne+index+5)<=14):
                if(Matrice[ligne][i] !=jou and Matrice[ligne][i]!= 0):
                    adversaire = True

                if(Matrice[ligne][i] == jou):
                    coequipier += 1
        if(adversaire == False and (colonne+index)>=0 and (colonne+index+5)<=14):
            points += 2**coequipier

        index += 1
    index = -4
    while(index <= 0):
        adversaire = False
        coequipier = 0
        for i in range((ligne+index),(ligne+index+5)):
            if((ligne+index)>=0 and (ligne+index+5)<=14):
                if(Matrice[i][colonne] !=jou and Matrice[i][colonne]!= 0):
                    adversaire = True

                if(Matrice[i][colonne] == jou):
                    coequipier += 1
        if(adversaire == False and (ligne+index)>=0 and (ligne+index+5)<=14):
            points += 2**coequipier

        index+=1
    index = 0
    while(index < 5):
        adversaire = False
        coequipier = 0
        for i in range(-4 + index,1+index):
            if((ligne+i)>=0 and (colonne+i)>=0 and (ligne+i)<=14 and (colonne+i)<=14):
                if(Matrice[ligne +i][colonne+i] !=jou and Matrice[ligne+i][colonne +i]!= 0):
                    adversaire = True

                if(Matrice[ligne+i][colonne+i] == jou):
                    coequipier += 1

        if(adversaire == False and (ligne+i)>=0 and (colonne+i)>=0 and (ligne+i)<=14 and (colonne+i)<=14):
            points += 2**coequipier

        index+=1
    if(TerminalTest(Matrice)==jou):
      points += 1000
    index = -4
    while (index <= 0):
        defenseur = False
        nb_adversaires = 0
        for i in range((colonne + index), (colonne + index + 5)):
            if ((colonne + index) >= 0 and (colonne + index + 5) <= 14):
                if (Matrice[ligne][i] != jou and Matrice[ligne][i] != 0):
                    nb_adversaires += 1

                if (Matrice[ligne][i] == jou):
                    defenseur = True
        if (defenseur == False and nb_adversaires == 3):
            points += 50
        if (defenseur == False and nb_adversaires == 4):
            points += 1000

        index += 1
    index = -4
    while (index <= 0):
        defenseur = False
        nb_adversaires = 0
        for i in range((ligne + index), (ligne + index + 5)):
            if ((ligne + index) >= 0 and (ligne + index + 5) <= 14):
                if (Matrice[i][colonne] != jou and Matrice[i][colonne] != 0):
                    nb_adversaires += 1

                if (Matrice[i][colonne] == jou):
                    defenseur = True
        if (defenseur == False and nb_adversaires == 3):
            points += 50
        if (defenseur == False and nb_adversaires == 4):
            points += 1000

        index += 1
    index = 0
    while(index < 5):
        defenseur = False
        nb_adversaires = 0
        for i in range(-4 + index,1+index):
            if((ligne+i)>=0 and (colonne+i)>=0 and (ligne+i)<=14 and (colonne+i)<=14):
                if(Matrice[ligne +i][colonne+i] !=jou and Matrice[ligne+i][colonne +i]!= 0):
                    nb_adversaires +=1

                if(Matrice[ligne+i][colonne+i] == jou):
                    defenseur = True

        if (defenseur == False and nb_adversaires == 3):
            points += 50
        if (defenseur == False and nb_adversaires == 4):
            points += 1000

        index+=1
    return points


def TerminalTest(Matrice):
    tailleM = 15
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
                    return jou
        for elem in cols:
            count = 0
            for x in elem:
                if(x == jou):
                    count +=1
                if(x !=jou):
                    count =0
                if(count == 5):
                    return jou
        for elem in Matrice:
            count = 0
            for x in elem:
                if(x == jou):
                    count +=1
                if(x !=jou):
                    count =0
                if(count == 5):
                    return jou
    verif = 0
    for i in range(tailleM):
        for j in range(tailleM):
            if(Matrice[i][j] == 0):
                verif += 1
    if(verif == 0):return -1
    return 0

def MaxValue(Matrice, tailleM,jou,p, profondeur, Alpha, Beta,tour,i,j):
    if(TerminalTest(Matrice) or profondeur == prof):
        return Utility(Matrice, tailleM,jou[p],i,j)
    res = Actions(Matrice, tailleM,tour)
    best = []
    
    for x in res:
        
        mm= MinValue(Result(copy.deepcopy(Matrice), x[0],x[1],jou[p]),tailleM,jou,(p+1)%2,profondeur+1, Alpha, Beta,copy.deepcopy(tour+1),x[0],x[1])
        if(mm > Beta):
            return mm
        
        best.append(mm)
    
    best = sorted(best,reverse=True)
    best = best[0]
    Alpha = best
    return best
def MinValue(Matrice, tailleM, jou,p, profondeur, Alpha, Beta, tour,i,j):
    if(TerminalTest(Matrice) or profondeur == prof ):
        return Utility(Matrice, tailleM,jou[p],i,j)
    res = Actions(Matrice, tailleM,tour)
    
    best = []
    
    for x in res:
       
        mm = MaxValue(Result(copy.deepcopy(Matrice), x[0],x[1],jou[p]),tailleM,jou,(p+1)%2,profondeur+1, Alpha, Beta,copy.deepcopy(tour+1),x[0],x[1])
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
    
    threat = ThreatSearch(Matrice, tailleM, 2)
    
    if(threat != [-9999999,-1,-1]):
        return threat
    for x in res:        
        
        mm = MinValue(Result(copy.deepcopy(Matrice), x[0],x[1],jou[p]),tailleM,jou,(p+1)%2, profondeur,math.inf,-math.inf,copy.deepcopy(tour+1),x[0],x[1])
        
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
        tour +=1
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
    print("+------------------------------------------------+")
    print("    A  B  C  D  E  F  G  H  I  J  K  L  M  N  O")
    for i in range(tailleM):
        if i<10:
            print(str(i)+"  "+str([Matrice[i][j] for j in range(tailleM)]))
        if i >10:
            print(str(i)+" "+str([Matrice[i][j] for j in range(tailleM)]))
    print("+------------------------------------------------+")

Main()
