import sys,string, math, itertools
from itertools import permutations,combinations

n,k = input().split()
n,k = int(n),int(k)
L1 = [ int(x) for x in input().split()]
L2 = list(combinations(L1,k))
L2 = list(itertools.combinations_with_replacement(L1,k))
out = []
for x in L2 :
    sum1 = sum(x)
    if sum1 not in out :
        out.append(sum1)
out.sort()
print(*out)
