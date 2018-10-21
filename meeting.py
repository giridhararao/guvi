n = int(input())
a=input().split()
b=input().split()
c=[]
d=[]
for i in range(0,n):
    c.append(int(a[i]))
    d.append(int(b[i]))
o = 0
for i in range(0,n-1) :
    y = 1
    x = d[i]
    for j in range(0,n) :
        if i != j :
            if c[j] >= x :
                y += 1
                x = d[j]
    if y > o :
        o = y
print(o)
