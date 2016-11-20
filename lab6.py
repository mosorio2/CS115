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

def count(S,N):
    print S
    if N==0:
        return S
    return count(increment(S),N-1)

def numToTernary(N):
    if N==0:
        return ''
    elif N%3==0:
        return numToTernary(N/3)+'0'
    elif N%3==1:
        return numToTernary(N/3)+'1'
    else:
        return numToTernary(N/3)+'2'

def ternaryToNum(S):
    if S=='':
        return 0
    elif S[-1]=='0':
        return 3*ternaryToNum(S[:-1])
    elif S[-1]=='1':
        return 3*ternaryToNum(S[:-1])+1
    else:
        return 3*ternaryToNum(S[:-1])+2


        
