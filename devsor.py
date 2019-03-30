import sys,string, math

n,k = input().split()
n,k = int(n),int(k)
out = [ int(x) for x in input().split()]
for i in range(0,n-1) :
    for j in range(i+1,n) :
        if out[i] > out[j] :
            out[i], out[j] = out[j], out[i]
print(*out)
