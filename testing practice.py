def my_ord(c):
    return ord(c)+1

def my_chr(n):
    return chr(n)

def test():
    try:
        print 3/0
    except:
        print "or na"
    try:
        assert my_chr(my_ord('A'))=='A'
        print "Test 1 passed with input A."
    except:
        print "Test 1 failed with input A."
        print "Expected: A, received:", my_chr(my_ord('A'))

test()




        
    
