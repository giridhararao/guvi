n,k = input().split()
n,k = int(n),int(k)
L = [int(x) for x in input().split()]
L.sort()
out = 0
a = n // 3
for i in range(0,a) :
    L2 = L[3*i : 3*(i+1)]
    if 5-max(L2) >= k :
        out += 1
print(out)
