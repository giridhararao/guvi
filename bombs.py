import sys,string, math, itertools

n = int(input())
out = []
if n==2 :
    print('3')
    print('2 1 2')
    sys.exit()
if n==3 :
    print('4')
    print('2 1 3 2')
    sys.exit()
k = n//2
for i in range(2,n+1,2) :
    out.append(i)
for i in range(1,n,2 ) :
    out.append(i)
for i in range(2,n+1,2 ) :
    out.append(i)
print(len(out))
print(*out)
