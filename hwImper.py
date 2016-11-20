# hwImper.py
# Michael Osorio Nov 2012, rev Oct 2013, Oct 2014
#10/29/14
#I pledge my honor that I have adided by the Stevens Honor System.
 
# Objectives: get familiar with imperative style and for- and while-loops.

# Instructions: Submit a copy of this file, with your name instead of mine,
# and with the incomplete functions completed.  Don't change the functions
# that are already implemented.  
# You should add code for testing.

# Search for "TO DO" to find the incomplete functions.

############
# Exercise 0
# Study function questify().  Then implement questifyAlt() so that it gives
# the same results as questify(), using map and lambda but no helping function.
# Hint: adapt the body of addQuestmark().
############

def questify(strs):
    ''' Assume strs is a list of strings.  Return a list of
        the same strings but with ? suffixed to each.'''
    def addQuestmark(str):
        '''add question mark to a string'''
        return str + '?'

    return map(addQuestmark, strs)

def questifyAlt(strs):
    ''' Same as questify.'''
    return map(lambda x: x + '?', strs)


############
# Exercise 1
# Study functions leppard() and catenate().  Implement catenateLoop(), without
# using recursion or reduce or any built-in Python function.  Instead, use a 
# loop.  In some ways your code will resemble the body of leppard().
# If you prefer, you can follow the style of leppardIndex() but I suggest not.
############

def leppard(inputString):
    ''' Mystery.'''
    outputString = ""
    for symbol in inputString:    
        if symbol == "o":
           outputString = outputString + "ooo"
        else:
           outputString = outputString + symbol
    print outputString

def leppardIndex(inputString):
    ''' Same as leppard(), but using an integer index rather than directly
        referring to elements of the input string.'''
    outputString = ""
    for i in range(len(inputString)):
        if inputString[i] == "o":
           outputString = outputString + "ooo"
        else:
           outputString = outputString + inputString[i]
    print outputString

def catenate(strs):
    ''' Assume strs is a list of strings.
        Return a single string, their catenation.'''
    if strs == []:
       return ""
    else:
       return reduce(lambda s, t: s + t,   strs)

def catenateLoop(strs):
    ''' same as catenate'''
    if strs == []:
        return ''
    catenate = ''
    for i in strs:
        catenate += i
    return catenate

def catenateTest():
    ''' Test consistency between two versions of catenate.'''
    test0 = ["one ", "test ", "case"]
    test1 = []
    test2 = ["", "xxx", "", "yyy"]
    for t in [test0, test1, test2]:  
        print "catenateTest: Checking test case ", t
        assert catenate(t) == catenateLoop(t)
        print 'Success'
        

############
# Exercise 2
# Implement letterScoreLoop using --you guessed it-- a loop instead of recursion.  
# Also, do not use map or reduce.
############

scrabbleScores = [ ["a", 1], ["b", 3], ["c", 3], ["d", 2], ["e", 1], ["f", 4], ["g", 2], ["h", 4], ["i", 1], ["j", 8], ["k", 5], ["l", 1], ["m", 3], ["n", 1], ["o", 1], ["p", 3], ["q", 10], ["r", 1], ["s", 1], ["t", 1], ["u", 1], ["v", 4], ["w", 4], ["x", 8], ["y", 4], ["z", 10] ]

aDictionary = ["a", "am", "at", "apple", "bat", "bar", "babble", "can", "foo", "spam", "spammy", "zzyzva"]

def letterScore(letter, scorelist): 
    '''
    Assume scorelist is a list of lists [ltr,val] where ltr is a single letter
    and val is a natural number.  Assume letter is a single letter string, that
    occurs in scorelist.  Return the associated value.
    '''
    if letter == scorelist[0][0]:
        return scorelist[0][1]
    else:
        return letterScore(letter, scorelist[1:])

def letterScoreLoop(letter, scoreList):
    ''' Same as letterScore'''
    # It may be helpful to use an if-statement without an else.
    for i in scoreList:
        if letter == i[0]:
            return i[1]

def letterScoreTest():
    ''' Test consistency between two versions of letterScore.'''
    test1 = ['a',scrabbleScores]
    test2 = ['h',scrabbleScores]
    test3 = ['z',scrabbleScores]

    for i in [test1, test2, test3]:
        assert letterScore(i[0],i[1]) == letterScoreLoop(i[0],i[1])
        print 'Success'

############
# Exercise 3
# Implement wordScoreLoop using a loop instead of recursion.  (And don't
# use map or reduce.)
# Use letterScore() or letterScoreLoop(); it shouldn't matter which one.
############

def wordScore(S, scorelist):   
    ''' Assume S is a string and scorelist is in the format above and 
        includes every letter in S.  Return the scrabble score of that string.'''
    if S == '': 
        return 0
    else:
        return letterScore(S[0], scorelist) + wordScore(S[1:], scorelist)

def wordScoreLoop(S, scoreList): 
    ''' same as wordScore'''
    if S == '':
        return 0
    score = 0
    for i in S:
        score += letterScoreLoop(i, scoreList)
    return score

def wordScoreTest():
    ''' Test consistency between two versions of wordScore.'''
    test1 = ['apple',scrabbleScores]
    test2 = ['hello',scrabbleScores]
    test3 = ['zebra',scrabbleScores]

    for i in [test1, test2, test3]:
        assert wordScore(i[0],i[1]) == wordScoreLoop(i[0],i[1])
        print 'Success'


############
# Exercise 4
# Implement wordsWithScoreLambda using a lambda instead of the helper scoreWord.
############

def wordsWithScore(dict, scores):
    '''
    Assume dict is a list of words and scores is a list of [letter,number] pairs.
    return a copy of the dictionary, annotated so each word is paired with its
    value. For example, wordsWithScore(scrabbleScores, aDictionary) should return
    [["a", 1], ["am", 4], ["at", 2] ...etc... ]
    '''

    def scoreWord(wrd):
      return [ wrd, wordScore(wrd, scores) ]
        
    return map(scoreWord, dict)

def wordsWithScoreLambda(dict, scores):
    ''' same as wordsWithScore'''
    return map(lambda word: [word, wordScore(word, scores)], dict)


############
# Exercise 5
# Implement wordsWithScoreLoop using a loop instead of map or recursion.
# Be careful NOT to change the dictionary.  
############

def wordsWithScoreLoop(dict, scores):
    '''Same as wordsWithScore'''
    output = []
    for i in dict:
        output += [[i, wordScoreLoop(i, scores)]]
    return output

def wordsWithScoreTest():
    test = [aDictionary,scrabbleScores]

    assert wordsWithScore(test[0],test[1]) == wordsWithScoreLambda(test[0],test[1]) == wordsWithScoreLoop(test[0],test[1])
    print 'Success'
   

###########
# Main test
###########

def testAll():
    catenateTest()
    letterScoreTest()
    wordScoreTest()
    wordsWithScoreTest()

