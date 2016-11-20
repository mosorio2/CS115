>>> def mult(x,y):
    """returns the product of x and y"""
    return x*y
def factorial(n):
    """returns the factorial of n"""
    lst=range(1,n+1)
    return reduce(mult, lst)

#2
def add(x,y):
    """returns the sum of x and y"""
    return x+y
def divide(x,y):
    """returns the quotient of x and y"""
    return x/y
def mean(L):
    """returns the average of list L"""
    lst2=float(len(L))
    total=reduce(add, L)
    return total/lst2

#3
def divides(n):
    def div(k):
        return n % k == 0
    return div
def prime(n):
    """returns true or false depending on if n is prime or not"""
    if n<=1:
        return False
    if n==2:
        return True
    lst3=map(divides(n),range(2,n))
    lst4=reduce(add,lst3)
    if lst4==0:
        return True
    else:
        return False
