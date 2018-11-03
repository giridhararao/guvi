def length(a,b):
    x=1
    y=0
    for i in range(1,b):
        if(a[i]>=a[i-1]):
            x=x+1
        else:
            x=1
        if(x>y):
            y=x
    return(y)
a=int(input())
b=input().split()
c=[]
for i in range(0,a):
    c.append(int(b[i]))
d=length(c,a)
print(d)
