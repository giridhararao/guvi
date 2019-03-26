    
import sys,string

s1,s2 = input().split()
n1 = len(s1)
n2 = len(s2)
a = []
if n1 == n2 :
    for i in range(0,n1) :
        a.append(s1[i])
        a.append(s2[i])
elif n1 < n2 :
    for i in range(0,n1) :
        a.append(s1[i])
        a.append(s2[i])
    k = 1
    i += 1
    for j in range(i,n2) :
        a.append(str(k))
        a.append(s2[i])
        k += 1
        i += 1
else :
    for i in range(0,n2) :
        a.append(s1[i])
        a.append(s2[i])
    k = 1
    i += 1
    for j in range(i,n1) :
        a.append(s1[i])
        a.append(str(k))
        k += 1
        i += 1

out = ''.join(a)
print(out)
