#Michael Osorio

def change(x,coins):
    '''returns the minimum number of coins which add up to a given number called x'''
    if x==0:
        return 0
    if coins==[]:
        return float('inf')
    elif coins[0] > x:
        return change(x,coins[1:])
    else:
        loseIt=change(x, coins[1:])
        useIt= 1 + change(x-coins[0], coins[0:])
        return min(loseIt,useIt)

def giveChange(x, coins):
    '''returns the minimum number of coins which add up to a given number x, and returns the coins used'''
    if x==0:
        return 0
    if coins==[]:
        return float('inf')
    elif coins[0] > x:
        return giveChange(x,coins[1:])
    else:
        loseIt=giveChange(x, coins[1:])
        useIt=giveChange(x-coins[0], coins[0:])
        useIt=[1+useIt[0],use[1]+[coins[0]]]
    return min(loseIt[0],useIt[0])
    if useIt[0]>loseIt[0]:
            return loseIt
        


       
       
                      
    
    
    
   
    
        
        
