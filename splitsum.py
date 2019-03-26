import sys,string

a = int(input())
b = [ int(x) for x in input().split()]
out = 0
for i in range(0,a-2) :
    for j in range(i+1,a-1) :
        for k in range(j+1,a) :
            if b[i] + b[j] == b[k] :
                out += 1
print(out)
