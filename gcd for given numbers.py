def gcd(a):
    b=1
    for i in range(2,min(a)+1):
        if(all([x%i==0 for x in a])):
            b=i
    return(b)
n,q=input().split()
n=int(n)
q=int(q)
a=[]
out=[]
c=input().split()
for i in range(0,n):
    a.append(int(c[i]))
for i in range(0,q):
    e,f=input().split()
    e=int(e)
    f=int(f)
    o=gcd(a[e-1:f])
    out.append(o)
for i in out:
    print(i)
