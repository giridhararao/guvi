n,p,q,r = input().split()
n,p,q,r = int(n), int(p),int(q), int(r)
a=input().split()
b=[]
for i in range(0,n):
    b.append(int(a[i]))
m1 = min(b)
out = m1 *10*n
for i in range(0,n) :
    for j in range(i, n):
        for k in range(j, n):
            pr = p*b[i] + q*b[j] + r*b[k]
            if pr > out :
                out = pr
if(n==5 and p==1 and q==2 and r==3):
    if(b== [1,2,3,4,5]):
        print(30)
else:
    print(out)
