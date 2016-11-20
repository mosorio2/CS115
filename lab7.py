def isOdd(n):
    if n%2==1:
        return True
    else:
        return False

def numToBinary(N):
    if N==0:
        return ''
    elif isOdd(N):
        return numToBinary(N/2)+'1'
    else:
        return numToBinary(N/2)+'0'

def binaryToNum(S):
    if S=='':
        return 0
    elif S[-1]=='0':
        return 2*binaryToNum(S[:-1])
    else:
        return 2*binaryToNum(S[:-1])+1

def increment(S):
    x=binaryToNum(S)+1
    y=numToBinary(x)
    return incrementPad(y)
def incrementPad(S):
    if len(S)>=8:
        return S
    return incrementPad('0'+S)


def TcToNum(S):
    if S[0]=='0':
        return binaryToNum(S)
    else:
        return binaryToNum(S) - 256


def NumToTc(N):
    if N>127 or N< -128:
        return 'Error'
    if N<0:
        return numToBinary(N+256)
    else:
        return increment(numToBinary(N-1))

   
# Now do the folllwing exercises

# Step 1. 

# Implement the following.  

def combs(n):
    '''Assume n >= 1.  Return a list of all lists of n bits, in binary
    numerical order.  For example combs(2) is [[0,0],[0,1],[1,0],[1,1]].
    Hints:  Think recursively, sort of like use-it-or-lose-it.
    Use map and lambda and also recursive call combs(n-1).'''
    if n==1:
        return [[0],[1]]
    else:
        x=map(lambda x: [x+[0],x+[1]], combs(n-1))
        y=reduce(lambda t,y: t+y, x)
        return y
    


    
# Step 2.

# The following function is intended to be applied to booleans.
# For example, func0(1,0,1) returns 1 (which may display as True).

def func0(x,y,z): return x and (y or z)

# We would like to try this function on all possible inputs.
# Try this:  map(func0, combs(3))
# Think about why it doesn't work.

# Try this, which works:  
#      map(lambda args: func0(*args), combs(3))
# The syntax *args says to pass the elements of args to func0 as three
# separate arguments, e.g., func0(*[1,0,1]) is func0(1,0,1).

# Implement the following.

def func0table():
    '''Return the list [([0,0,0], 0), ([0,0,1], 0), ... , ([1,1,1], 1)]
        which represents the truth table for func0.  In other words
        list all the tuples ([x,y,z], func0(x,y,z)).
        Hint: Use map, similarly to 'Try this' above.
    '''
    return map(lambda args: (args, func0(*args), combs(3)))

# Here is a function that displays the result as a table.

def showTable(lst):
    '''Assume lst is in the format returned by func0table(). Print it.
    '''
    if lst == []: return None
    else:
        print lst[0][0], lst[0][1]
        showTable(lst[1:])

# Step 3.

# Based on the truth table for func0, we defined the following alternate
# implementation for the same function. (It's called the 'minterm principle.')
# Have a look:

def func0alt(x,y,z):
    return ( (x and not y and z)
             or (x and y and not z)
             or (x and y and z) )

# Implement this test that compares func0 with func0alt.

def func0test():
    '''Applies func0 and func0alt to all possible inputs.  Returns True
        if they agree in every case, otherwise False.  
        Hint: one way uses map and then reduce.'''

    def myAnd(x,y): 
        ''' x and y.  For use with reduce.'''
        return x and y

    return reduce(myAnd, map(lambda args: func0(*args)==func0alt(*args),combs(3)))

# Step 4.

# You will play the same game with this function:
def func1(x,y): return x or (y and x)

# Implement these functions:

def func1table():
    '''Return a table of values of func1, 
         so they can be displayed using showTable.
    '''
    return map(lambda args:(args, func1(*args), combs(2)))

def func1alt(x,y):
    '''Return func1(x,y), computed based on the minterm principle.
    '''
    return ((x and not y)
            or (x and y))
            

def func1test():
    '''Apply func1 and func1alt to all possible inputs.  Return True or
        False depending on whether they agree in every case.
    '''
    def myAnd(x,y): 
        ''' x and y.  For use with reduce.'''
        return x and y
    
    return reduce(myAnd, map(lambda args: func1(*args)==func1alt(*args),combs(2)))

    


            

