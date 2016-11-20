def knapsack(capacity,itemlist):
    '''returns the max value and the items that make up said value, without exceeding the capacity of the knapsack'''
    if itemlist==[]:
        return [0,[]]
    elif capacity==0:
        return [0,[]]
    elif itemlist[0][0]>capacity:
        return knapsack(capacity,itemlist[1:])
    else:
        loseit= knapsack(capacity,itemlist[1:])
        useit=knapsack(capacity-itemlist[0][0], itemlist[1:])
        useit = [useit[0]+itemlist[0][1], itemlist[0:][0:]]
        return max(useit,loseit)        

def fib(n):
    if n==1:
        return[1]
    elif n==2:
        return[1,1]
    else:
        x=fib(n-1)
        return x+[x[-1]+x[-2]]
    
