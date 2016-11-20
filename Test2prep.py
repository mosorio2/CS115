def tw(f,L):
    if L==[]:
        return []
    elif f(L[0]):
        return [L[0]]+tw(f,L[1:])
    else:
        return []
    
def change(a,c):
    if a==0:
        return 0
    elif c==[]:
        return float('inf')
    elif c[0]>a:
        return change(a,c[1:])
    else:
        use=1+ change(a-c[0],c)
        lose=change(a,c[1:])
        return min(use,lose)

def ntb(n):
    if n==0:
        return ''
    elif n%2=0:
        return ntb(n/2)+'0'
    else:
        return ntb(n/2)+'1'


    
    
        
