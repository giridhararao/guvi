n,k = map(int,input().split())
a = list(map(int,input().split()))
b = [ (x,abs(x-k)) for x in a]
c = sorted(b, key=lambda x : x[1])
g= 0
o = []
for i in range(0,len(c)) :
    if c[i][1] == 0 : continue
    o.append(c[i][0])
    g += 1
    if g == 3 : break
print(" ".join(str(x) for x in o))
