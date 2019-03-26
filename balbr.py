    
import sys,string, math
from itertools import permutations,combinations
def balbr(s) :
    b1=0
    n = len(s)
    if s[0]== '}' :
        return False
    for i in range(0,n) :
        if s[i] == '{' :
            b1 += 1
        if s[i] == '}' :
            b1 -= 1
        if b1<0 :
            return False
    if b1==0 :
        return True
    else :
        return False

n = int(input())
s = '{}'*n
L1 = list(permutations(s))
L2 = [''.join(x) for x in L1]
L3 = []
for i in L2 :
    if balbr(i) :
        L3.append(x)
out = []
for i in L3 :
    if i not in out :
        out.append(i)
for i in L4 :
    print(i)
