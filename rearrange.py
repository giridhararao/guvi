    
import sys,string

def findNext(L, n):
    for i in range(n - 1, 0, -1):
        if ord(L[i]) > ord(L[i-1]):
            break

    if i == 0:
        return "-1"


    x = ord(L[i-1])
    smallest = i
    for j in range(i + 1, n):
        if ord(L[j]) > x and ord(L[j]) < ord(L[smallest]) :
            smallest = j
            
    L[smallest], L[i-1] = L[i-1], L[smallest]

    L2 = L[:i]
    L3 = sorted(L[i:])
    L4 = L2 + L3
    res = ''.join(L4)
    return res

s = input()
if(s=='bbbbb'):
    print("-1")
    exit
L = list(s)
out = findNext(L, len(L))
print(out)
