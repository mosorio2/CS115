# CS 115 Homework 3     (your file should be named hw3solution.py)
# Michael Osorio
# 9/22/14
# I pledge my honor that I have abided by the Stevens Honor System..


############
# PROBLEM 0 
############
def giveChange(x, Coins):
    if x == 0:
        return [0,[]]
    if Coins == []:
        return [float('inf'),[]]
    elif Coins[0] > x:
        return giveChange(x, Coins[1:])
    else:
        loseIt = giveChange(x, Coins[1:])
        useIt = giveChange(x - Coins[0], Coins)
        useIt = [1 + useIt[0], useIt[1] + [Coins[0]]]
        if useIt[0] > loseIt[0]:
            return loseIt
        else:
            return useIt
print "Testing giveChange"
print giveChange(32, [1,5,10,25,50])


############
# PROBLEM 1
############

# Implement wordsWithScore() which is specified below.
# Hints: Use map.  And use some of the functions you did for
# homework 3 (Scrabble Scoring).  As always, include any helper
# functions in this file, so we can test it.

# Here's the list of letter values and a small dictionary to use.

scrabbleScores = [ ["a", 1], ["b", 3], ["c", 3], ["d", 2], ["e", 1], ["f", 4], ["g", 2], ["h", 4], ["i", 1], ["j", 8], ["k", 5], ["l", 1], ["m", 3], ["n", 1], ["o", 1], ["p", 3], ["q", 10], ["r", 1], ["s", 1], ["t", 1], ["u", 1], ["v", 4], ["w", 4], ["x", 8], ["y", 4], ["z", 10] ]

aDictionary = ["a", "am", "at", "apple", "bat", "bar", "babble", "can", "foo", "spam", "spammy", "zzyzva"]

def letterScore(letter, scoreList):
    "returns a character with the score (value) of that character"""
    if(letter == scoreList[0][0]):
        return scoreList[0][1]
    return letterScore(letter, scoreList[1:])

def wordScore(S, scoreList):
    """returns a string with total score (value) of the letters in the string"""
    if(S == ""):
        return 0
    return letterScore(S[0], scoreList) + wordScore(S[1:], scoreList)

def wordsWithScore(dict, scores):
    """List of words in dict, with their Scrabble score.

    Assume dict is a list of words and scores is a list of [letter,number] pairs.
    return the dictionary annotated so each word is paired with its value.
    For example, wordsWithScore(scrabbleScores, aDictionary) should return
    [["a", 1], ["am", 4], ["at", 2] ...etc... ]
    """
    if dict == []:
        return []
    return [[dict[0],wordScore(dict[0],scrabbleScores)]] + wordsWithScore(dict[1:],scores)

print "Testing wordsWithScore"
print wordsWithScore(aDictionary,scrabbleScores)

############
# PROBLEM 2
############
def take(n, L):
    '''return the list L[0:n]'''
    if n == 0:
        return []
    return [L[0]] + take(n-1,L[1:])

# Code to use for testing
def testTake(n,L):
    '''computes L[0:n] using the function above and checks the answer'''
    if take(n,L)==L[0:n]:
        print "test ok"
    else: print "my test failed"


testTake(0, ["not", "it", "works", "!"])
testTake(2, ["not", "it", "works", "!"])
testTake(4, ["not", "it", "works", "!"])


############
# PROBLEM 3
############
def drop(n, L):
    '''return the list L[n:]'''
    if L == []:
        return []
    if n <= 0:
        return [L[0]] + drop(n, L[1:])
    return drop(n-1, L[1:])

def testDrop(n,L):
    '''computes L[n:] using the function above and checks the answer'''
    if drop(n,L)==L[n:]:
        print "test ok"
    else: print "my test failed"

testDrop(0, ["I", "am", "nearly", "done"])
testDrop(1, ["I", "am", "nearly", "done"])
testDrop(3, ["I", "am", "nearly", "done"])
