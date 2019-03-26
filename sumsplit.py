    
import sys,string

a = int(input())
b = [ int(x) for x in input().split()]
out = 0
for i in range(0,a-1) :
    for j in range(i+1,a) :
        if b[i] < b[j] :
            out += 1
print(out)
