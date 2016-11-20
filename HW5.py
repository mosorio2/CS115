# CS 115 HW 5
# Michael Osorio
# Oct 8, 2014
# I pledge my honor that I have abided by the Stevens Honor System.


import turtle


def svTree(trunkLength, levels):
    '''draws a stick figure of a tree'''
    if levels >=1:
        turtle.forward(trunkLength)
        turtle.right(45)
        svTree(trunkLength*0.5, levels-1)
        turtle.left(90)
        svTree(trunkLength*0.5, levels-1)
        turtle.right(45)
        turtle.backward(trunkLength)
        turtle.done

        svTree(128,6)

memo={0:0,1:1}
def fastFib(n):
    """Returns the nth fibonacci number using the memoization technique
    shown in class and lab. Assume that the 1st fibonacci number is 1 so fastFib(1) = 1,
    fastFIb(2) = 1 and fastFib(3) = 2"""
    if not memo.has_key((n)):
        memo[n]=fastFib(n-1)+fastFib(n-2)
    return memo[n]



