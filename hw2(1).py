#I pledge that I have abided by the Stevens Honor System. Anthony Picone and Michael Osorio

#A given list of scores for each letter
scrabbleScores = [ ["a", 1], ["b", 3], ["c", 3], ["d", 2], ["e", 1], ["f", 4], ["g", 2], ["h", 4], ["i", 1], ["j", 8], ["k", 5], ["l", 1], ["m", 3], ["n", 1], ["o", 1], ["p", 3], ["q", 10], ["r", 1], ["s", 1], ["t", 1], ["u", 1], ["v", 4], ["w", 4], ["x", 8], ["y", 4], ["z", 10] ]

from dict import *
import sys

sys.setrecursionlimit(10000)  # Allows up to 10000 recursive calls; the maximum permitted ranges from system to system


def letterScore(letter, scorelist):
    """Takes a letter, and returns the score for the letter"""
    if letter == scorelist[0][0]:
        return scorelist[0][1]
    return letterScore(letter, scorelist[1:])


def wordScore(S, scorelist):
    """Calculate the score of 's'"""
    if S == "":
        return 0
    return letterScore(S[0],scorelist) + wordScore(S[1:],scorelist)


#tester dictionary and rack used for some methods    
#Dictionary = [ "a","am","at","apple", "bat", "bar", "babble", "can", "foo", "spam", "spammy", "zzyzva"]
Rack = ['a','f','v','m']

#Helper Funtion from Lab

def ind(e,L):
    """Returns the index of e if e is in L"""

    if L == [] or L == "":
        return 0
    if e ==L[0]:
        return 0
    return ind(e,L[1:]) +1

def remove(e,L):
    """Removes the first instance of 'e' from the List 'L'"""
    if L ==[]:
       return []
    if L[0] == e:
        return L[1:]
    else:
        return [L[0]]+remove(e,L[1:])

################################


def wordPoss(word, Rack):
    """Checks to see if the given 'word' is possible to make from the given rack"""
    if word == "":
        return True
    if Rack==[]:
        return False
    elif word[0] in Rack:
        return wordPoss(word[1:], remove(word[0],Rack))
    return False

def scoreList(Rack):
    """returns the words possible and their score from the rack"""
    return words(Rack, Dictionary)

def words(Rack,D):
    """Takes Rack and returns a list of words that can be made with their score"""
    if D == []:
        return []
    if wordPoss(D[0],Rack) == True:
        return  [[D[0], wordScore(D[0],scrabbleScores)]]+ words(Rack,D[1:])
    return words(Rack,D[1:])

    
def my_max(L,N):
    """Compares the values of the scores of the letters and returns the greater"""
    if L[1] > N[1]:
        return L
    else:
        return N
    
    
def bestWord(Rack):
    """picks the word with the highest score and returns the word and it's score"""
    if Rack==[]:
        return []
    a = scoreList(Rack)
    if a == []:
        return []
    return reduce(my_max, a)
