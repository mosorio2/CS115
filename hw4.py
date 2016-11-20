def pAdd(L):
    """helper function that assists in adding terms"""
    if L == [1]:
        return []

    return [L[0] + L[1]] + pAdd(L[1:])


def pascal_row(n):
    """returns the nth row of the Pascal's triangle"""
    if n == 0:
        return [1]
    if n == 1:
        return [1,1]
    return [1] + pAdd(pascal_row(n - 1)) + [1]

print pascal_row(8)


def pascal_triangle (n):
    """returns a pascal's triangle up to row n"""
    def accum_helper(f,lst,n): # f is a index and j is the accum , lst is list
        if f >= n:
            return lst + [pascal_row(n)]
        return accum_helper(f+1,lst + [pascal_row(f)],n)
    return accum_helper(0,[], n )

print pascal_triangle(3)
