from random import randint


def createDecks():
    P = []
    PA = []
    PB = []
    
    #création du jeu de carte
    for i in range(1,14): 
        for j in range(1,5):
            P.append(i)
    
    #mélange des cartes
    for i in range(1,101):
        n = randint(0,51)
        o = randint(0,51)
        P[n], P[o] = P[o], P[n]
    
    #distribution des cartes
    for i in range(1,27):
        PA.append(P[i])
        del(P[i])
    PB = P
    return P, PA, PB

def cardAWins(currentCardB, PA, PB):
   PA.append(currentCardB)
   PA.insert(len(PA)-1, PA.pop(0))
   PB.pop(0) 

def cardBWins(currentCardA, PA, PB):
   PB.append(currentCardA)
   PB.insert(len(PB)-1, PB.pop(0))
   PA.pop(0)

def draw(currentCardA, currentCardB, PA, PB, L):
    L.append(currentCardA)
    L.append(currentCardB)
    PA.pop(0)
    PB.pop(0)
    hiddenCardA = PA[0]
    hiddenCardB = PB[0]
    print("A cache: ", hiddenCardA)
    print("B cache: ", hiddenCardB)
    L.append(hiddenCardA)
    L.append(hiddenCardB)
    PA.pop(0)
    PB.pop(0)
    print("A: ", PA[0])
    print("B: ", PB[0])
    
    
    
def bataille():
    
    P, PA, PB = createDecks()
    
    end = False
    
    while (end == False):
        
        currentCardA = PA[0]
        currentCardB = PB[0]
        print("A: ", currentCardA)
        print("B: ", currentCardB)
        
        #A gagne
        if currentCardA > currentCardB:
            cardAWins(currentCardB, PA, PB)
            print("A Wins: (", len(PA), " cards left)",)
            
        #B gagne
        elif currentCardB > currentCardA:
            cardBWins(currentCardA, PA, PB)
            print("B Wins: (", len(PB), " cards left)",)
        
        #égalité
        else:
            
            L = []
            while currentCardA == currentCardB:
                try:
                    draw(currentCardA, currentCardB, PA, PB, L)
                    currentCardA = PA[0]
                    currentCardB = PB[0]
                except:
                    end = True
                    if len(PA) == 0:
                        print("B a gagné")
                    if len(PB) == 0:
                        print("A a gagné")
                    return
                
            #A gagne
            if currentCardA > currentCardB:
                PA.extend(L)
                PA.pop(0)
                print("A Wins: (", len(PA), " cards left)",)
            
            #B gagne
            elif currentCardB > currentCardA:
                PB.extend(L)
                PB.pop(0)
                print("B Wins: (", len(PB), " cards left)",)
        
        if (len(PA) == 0 or len(PB) == 0):
            end = True
        
    if len(PA) == 0:
        print("B a gagné la partie")
    else:
        print("A a gagné la partie")
    return
            
            
            
            