# test1_Q78 - questions 7 and 8 on first exam, 2014

###########################################################################
# RULES: you can use Moodle to download this file and upload your solution.
# You can use IDLE to edit and run your program.  You should NOT look at 
# other programs in IDLE, you should NOT use any other programs, and you 
# should NOT use any notes or books.
# According to the Honor Code, you should report any student who appears
# to be violating these rules.
###########################################################################

#Michael Osorio
#I pledge my honor that I have abided by the Stevens Honor System.

########################
# Question 7 (20 points)
# Implement this function, using recursion and not using filter. 
########################


def remBad(strs):
    '''Assume strs is a list of strings.  Remove every occurrence of "bad"
    and leave the rest unchanged.'''
    if strs==[]:
        return []
    else:
        return strs[0]+remBad(strs[1:])





# Examples and a function to help testing

test1=["bad"]
ans1 = [] # this is the correct result for remBad(test1)
test2 = ["cat"]
ans2 = ["cat"]
test3 =["bad", "cat", "ate", "bad", "rat"]
ans3 = ["cat", "ate", "rat"]


def remBadTest():
    '''Test the remBad function.'''
    if remBad(test1) == ans1 and remBad(test2) == ans2 and remBad(test3) == ans3:
        print "success"
    else:
        print "test failed"


########################
# Question 8 (10 points)
# Implement this function using the 'filter' function, and not recursion.
########################


def remBadAlt(strs):
    '''same as remBad'''
    return filter('bad',remBadAlt(strs))

   

