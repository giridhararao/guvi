n = int(input())
a=input().split()
b=[]
c=[]
for i in range(0,n):
    b.append(int(a[i]))
for i in range(0,n):
    d = 1
    if b[i] > 0:
        sign = 1
    else:
        sign = -1
    for j in range(i+1,n) :
        if b[j] > 0:
            if sign == 1 :
                break
            else :
                d += 1
                sign = 1
        else:
            if sign == -1 :
                break
            else :
                d += 1
                sign = -1
    c.append(d)
print(" ".join(str(x) for x in c))
