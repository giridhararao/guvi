import sys,string, math, itertools

a,b = input().split()
a,b = int(a),int(b)
L = [ int(x) for x in input().split()]
for i in range(0,a) :
    if (86400-L[i]) >= b :
        print(i+1)
        sys.exit()
    b -= (86400-L[i])
