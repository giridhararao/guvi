n = int(input())
a = [int(x) for x in input().split()]
a.sort()
out = 0
for i in range(0,n) :
    if (a[i]-sum(a[:i])>= 0):
        out += 1
print(out)
