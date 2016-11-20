def mult(x,y):
    """returns the product of x and y"""
    return x*y
def add(x,y):
    """returns the sum of x and y"""
    return x+y
def dot(L,K):
    """returns the dot product of lists L and K"""
    if L==[] and K==[]:
        return 0.0
    else:
        return L[0]*K[0] + dot(L[1:],K[1:])

def explode(S):
    """returns a list of characters in a string"""
    if S=="":
        return[]
    else:
        return [S[0]]+explode(S[1:])

def ind(e,L):
    """returns the index of e if e is in L"""
    if L==[] or L=="":
        return 0
    elif e==L[0]:
        return 0
    else:
        return ind(e,L[1:])+1

def removeAll(e,L):
    """returns an identical list to L, except all elements identical to e are removed"""
    if L==[]:
        return []
    if e==L[0]:
        return removeAll(e,L[1:])
    else:
        return [L[0]]+removeAll(e,L[1:])

def even(x):
    if x%2==0:
        return True
    else:
        return False

def myFilter(f,L):
    """returns the parts of a list where the function is true and filters out the items that return false in the function"""
    if L==[]:
        return[]
    if f(L[0])== True:
        return[L[0]]+myFilter(f,L[1:])
    else:
         return myFilter(f,L[1:])

def deepReverse(L):
    """returns the reversal of a list where any second list contained in the original list is also reversed"""
    if L==[]:
        return[]
    if type(L[0])==type([1,2,3]):
        return deepReverse(L[1:])+[deepReverse(L[0])]
    else:
        return deepReverse(L[1:])+[L[0]]   
    
    

    
    
