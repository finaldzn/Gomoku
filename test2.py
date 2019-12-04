prof = 20
tailleM=15
def eval_function(state, jou):
    """ Simple heuristic to evaluate board configurations
        Heuristic is (num of 4-in-a-rows)*99999 + (num of 3-in-a-rows)*100 +
        (num of 2-in-a-rows)*10 - (num of opponent 4-in-a-rows)*99999 - (num of opponent
        3-in-a-rows)*100 - (num of opponent 2-in-a-rows)*10
    """
    if self.currentTurn == 1:
        o_color = 2
    elif self.currentTurn == 2:
        o_color = 1

    my_fours = self.checkForStreak(state,self.currentTurn, 5)
    #print my_fours
    my_threes = self.checkForStreak(state, self.currentTurn, 4)
    #print my_threes
    my_twos = self.checkForStreak(state,self.currentTurn, 3)
    #print my_twos
    opp_fours = self.checkForStreak(state, o_color, 5)
    #print opp_fours
    opp_threes = self.checkForStreak(state, o_color, 4)
    opp_twos = self.checkForStreak(state, o_color, 3)
    #if opp_fours > 0:
        #return -100000
    #else:
    return (my_fours * 10 + my_threes * 5 + my_twos * 2)- (opp_fours *10 + opp_threes * 5 + opp_twos * 2)

def checkForStreak(self, state, color, streak):
    count = 0
    # for each piece in the board...
    for i in range(15):
        for j in range(15):
            # ...that is of the color we're looking for...
            if state[i][j] == color:
                # check if a vertical streak starts at (i, j)
                count += self.verticalStreak(i, j, state, streak)
                # check if a horizontal four-in-a-row starts at (i, j)
                count += self.horizontalStreak(i, j, state, streak)
                # check if a diagonal (either way) four-in-a-row starts at (i, j)
                count += self.diagonalCheck(i, j, state, streak)
    # return the sum of streaks of length 'streak'
    return count

def verticalStreak(self, row, col, state, streak):
    consecutiveCount = 0
    for i in range(row, 15):
        if state[i][col] == state[row][col]:
            consecutiveCount += 1
        else:
            break

    if consecutiveCount >= streak:
        return 1
    else:
        return 0

def horizontalStreak(self, row, col, state, streak):
    consecutiveCount = 0
    for j in range(col, 15):
        if state[row][j]== state[row][col]:
            consecutiveCount += 1
        else:
            break

    if consecutiveCount >= streak:
        return 1
    else:
        return 0

def diagonalCheck(self, row, col, state, streak):
    
    total = 0
    # check for diagonals with positive slope
    consecutiveCount = 0
    j = col
    for i in range(row, 15):
        if j > 6:
            break
        elif state[i][j] == state[row][col]:
            consecutiveCount += 1
        else:
            break
        j += 1  # increment column when row is incremented

    if consecutiveCount >= streak:
        total += 1

    # check for diagonals with negative slope
    consecutiveCount = 0
    j = col
    for i in range(row, -1, -1):
        if j > 6:
            break
        elif state[i][j] == state[row][col]:
            consecutiveCount += 1
        else:
            break
        j += 1  # increment column when row is incremented

    if consecutiveCount >= streak:
        total += 1

    return total
def Actions(Matrice, tailleM,tour):
    valeur = []
    if(tour >3 ):
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
def MiniMaxDecision(Matrice, tailleM,var, profondeur,tour):
    res = Actions(Matrice, tailleM,tour)    
    point =[]
    jou=[1,2]
    p=var
    
    for x in res:        
        
        mm = MinValue(Result(copy.deepcopy(Matrice), x[0],x[1],jou[p]),tailleM,jou,(p+1)%2, profondeur,math.inf,-math.inf,copy.deepcopy(tour+1),x[1],x[0])
        
        point.append([mm,x[0],x[1]])
    
    point = sorted(point, key=lambda l:l[0], reverse = True)
    print("POSSSIBILITES : ")
    print(point)
    return point[0]
def MaxValue(Matrice, tailleM,jou,p, profondeur, Alpha, Beta,tour,i,j):
    if(TerminalTest(Matrice)==jou[p] or profondeur == prof):
        return eval_function(Matrice,jou[p])
    res = Actions(Matrice, tailleM,tour)
    best = []
    
    for x in res:
        
        mm= MinValue(Result(copy.deepcopy(Matrice), x[0],x[1],jou[p]),tailleM,jou,(p+1)%2,profondeur+1, Alpha, Beta,copy.deepcopy(tour+1),x[1],x[0])
        if(mm > Beta):
            return mm
        
        best.append(mm)
    
    best = sorted(best,reverse=True)
    best = best[0]
    Alpha = best
    return best
def MinValue(Matrice, tailleM, jou,p, profondeur, Alpha, Beta, tour,i,j):
    if(TerminalTest(Matrice)==jou[p] or profondeur == prof ):
        return Utility(Matrice, tailleM,jou[p],copy.deepcopy(i),copy.deepcopy(j))
    res = Actions(Matrice, tailleM,tour)
    
    best = []
    
    for x in res:
       
        mm = MaxValue(Result(copy.deepcopy(Matrice), x[0],x[1],jou[p]),tailleM,jou,(p+1)%2,profondeur+1, Alpha, Beta,copy.deepcopy(tour+1),x[1],x[0])
        if(mm < Alpha):
            return mm
        best.append(mm)
    
    best = sorted(best)
    best = best[0]
    Beta = best
    return best