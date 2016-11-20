def mult(c,n):
    result=0
    for x in range(n):
        result=result+c
    return result


def update(c,n):
    z=0
    for x in range(n):
        z=z**2+c
    return z


def inMSet(c,n):
    z=0
    for x in range(n):
        z=z**2+c
        if abs(z)>2:
            return False
    return True

from cs5png import *

def weWantThisPixel(col,row):
    if col%10==0 and row%10==0:
        return True
    else:
        return False

def test():
    width=300
    height=200
    image= PNGImage(width,height)
    for col in range(width):
        for row in range(height):
            if weWantThisPixel(col,row)==True:
                image.plotPoint(col,row)
    image.saveFile()
    
