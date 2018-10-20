alp="ABCDEFGHIJKLMNOPQRSTUVWXYS"
a=input()
b=[]
c=[]
d=[]
for i in range(0,len(alp)):
    d.append(alp[i])
for i in range(0,len(a)):
    b.append(a[i])
for i in b:
    if(i=="X"):
        c.append("A")
    elif(i=="Y"):
        c.append("B")
    elif(i=="Z"):
        c.append("C")
    else:
        for j in range(0,len(d)):
            if(i==d[j]):
                c.append(d[j+3])
                break
print("".join(str(x) for x in c))
