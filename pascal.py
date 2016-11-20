def pascal_row(num):
    if num == 0:
        return [1]
    if num == 1:
        return [1,1]
    def phelper(l):
        if l == []:
            return []
        if l[1:] == []:
            return []
        return [l[0]+l[1]]+ (phelper(l[1:]))
    return [1] + phelper(pascal_row(num-1)) + [1]
print pascal_row(5)


def pascal_triange (n):
    def accum_helper(f,lst,n): # f is a index and j is the accum , lst is list
        if f >= n:
            return lst + [pascal_row(n)]
        return accum_helper(f+1,lst + [pascal_row(f)],n)
    return accum_helper(0,[], n )

print pascal_triange(3)
