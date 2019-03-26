import sys,string, itertools

a = int(input())
a = [ int(x) for x in input().split()]
Li = [i for i in range(0,len(a))]
while len(a) > 1 :
    L2 = []
    L2i = []
    for i in range(1,len(a),2) :
        L2.append(a[i])
        L2i.append(Li[i])
   
    a = L2[:]
    Li = L2i[:]
print(a[0])
