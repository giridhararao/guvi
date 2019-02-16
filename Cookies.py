import sys,string
a,b = input().split()
a,b = int(a),int(b)
L1 = [ int(x) for x in input().split()]
L2 = [ int(x) for x in input().split()]
out = 0
for i in range(0,a) :
    L3 = L2[:]
    L3[i] += b
    L4 = []
    for j in range(0,a) :
        L4.append(L3[j]//L1[j])
    min1 = min(L4)
    if min1 > out :
        out = min1
print(out)
