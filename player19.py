n=int(input())
i=1
a=[]
while(i<=n):
    k=0
    if(n%i==0):
        j=1
        while(j<=i):
            if(i%j==0):
                k=k+1
            j=j+1
        if(k==2):
            a.append(i)
    i=i+1
print(" ".join(str(x) for x in a))
