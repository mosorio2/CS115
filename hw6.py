#Michael Osorio
#CS 115
#I Pledge my honor that I have abided by the Stevens Honor System.
#10/15/14
def isOdd(n):
    '''checks if a number is odd'''
    if n % 2 == 0:
        return False
    else:
        return True

def numToBinary(N):
    '''converts a given decimal number into a string bits'''
    if N == 0:
        return ''
    if isOdd(N):
        return numToBinary(N/2)+'1' 
    else:
        return numToBinary(N/2)+'0'


def binaryToNum(S):
    '''converts a string of binary digits into a decimal'''
    if S == '':
        return 0
    elif S[-1] == '0':
        return 2 * binaryToNum(S[:-1])
    else:
        return 2 * binaryToNum(S[:-1]) + 1


k = 5 
a = 2**k -1 

def counter(s):
    '''will count the number of the repeated digits'''
    if s == '':
        return 0
    elif len(s) == 1:
        return 1
    elif s[0] == s[1]:
        return 1 + counter(s[1:])
    else:
        return 1

def lister(s):
    '''turns string into list with digit as the first part and the number of times it appears in the series in a row'''
    if s == '':
        return []
    n = counter(s)
    return breaker([s[0],n]) + lister(s[n:])

def breaker(L):
    '''if the list has a second element bigger than the encoding allows, it breaks it up'''
    if L[1] > a:
        L = [[L[0],a]] + breaker([L[0],L[1]-a])
        return L 
    else:
        return [L]

def makeKBits(n):
    '''changes a binary number into binary with k bits'''
    if len(numToBinary(n)) <= k:
        return '0'* (k-len(numToBinary(n))) + numToBinary(n)

def printer(L):
    '''prints a section of the list into the encoded part'''
    if L[0] == '0':
        return '0' + makeKBits(L[1])
    else:
        return '1' + makeKBits(L[1])

def combineStrings(L):
    '''creates a string by combinging the strings in the entered list'''
    if L ==[]:
        return ''
    return L[0] + combineStrings(L[1:])

def compress(s):
    '''compresses a sequence of binary digits into a condensed version'''
    x = lister(s)
    y = map(printer,x)
    return combineStrings(y)


def uncompress(s):
    '''takes a compressed sequence of binary digits and uncompresses them'''
    if s == '':
        return ''
    else:
        return s[0] * binaryToNum(s[1:k+1]) + uncompress(s[k+1:])

def compression(s):
    '''returns the ratio of the compressed string to the uncompressed string'''
    return float(len(compress(s)))/len(s)
    
    
