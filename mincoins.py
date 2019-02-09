import sys, string, math
def minco(coi, m, V):
    if (V == 0):
        return 0
    res = sys.maxsize
    for i in range(0, m):
        if (coi[i] <= V):
            sub_res = minco(coi, m, V - coi[i])

            
            if (sub_res != sys.maxsize and sub_res + 1 < res):
                res = sub_res + 1
    return res
n,V = input().split()
n,V = int(n), int(V)
coi = [ int(x) for x in input().split()]
print( minco(coi, n, V))
