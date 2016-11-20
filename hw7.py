#Michael Osorio
#CS 115
#10/22/14
#I pledge my honor that I have abided by the Stevens Honor System.

def isOdd(N):
    if N%2==1:
        return True
    else:
        return False

#1
    
def numToBase(N,B):
    '''takes as input a non-negative interger N and a base B that is between 2 and 10 and returns a string representing N in base B.'''
    if N==0:
        return ''
    else:
        return numToBase(N/B,B)+str(N%B)

#2

def baseBToNum(S,B):
    '''takes as input a string S and a base B where S represents a number in base B (between 2 and 10)'''
    if S=='':
        return 0
    else:
        return B*baseBToNum(S[:-1],B)+int(S[-1])

#3

def baseToBase(B1,B2,SinB1):
    '''takes in base B1 and base B2 and string SinB1, representing a number in base B1. This should return a string representing the same number in B2.'''
    x=baseBToNum(SinB1,B1)
    return str(numToBase(x,B2))
        
#4

def add(S,T):
    '''adds two binary strings and returns their sum in binary'''
    x=baseBToNum(S,2)
    y=baseBToNum(T,2)
    z=x+y
    return numToBase(z,2)

#5

def addB(S,T):
    '''adds two binary numbers together without converting to base ten'''
    if S=='':
        return T
    if T=='':
        return S
    elif int(S[-1])+int(T[-1])==1:
        return addB(S[:-1],T[:-1])+'1'
    elif int(S[-1])+int(T[-1])==0:
        return addB(S[:-1],T[:-1])+'0'
    return carry(S[-1],T[-1],1)+'0'

def carry(S,T,A):
    '''helps add when values are carried over'''
    if T=='' or S=='':
        return 0
    if int(S[-1])+int(T[-1])==2:
        return '10'
    if int(S)+int(T)+1==3:
        return '11'
    else:
        return '1'
    

