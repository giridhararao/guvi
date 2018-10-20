l,r=input().split()
l=int(l)
r=int(r)
a=[]
b=[]
c=[]
for i in range(1,l+1):
	if l%i==0:
		a.append(i)
for i in range(1,r+1):
	if r%i==0:
		b.append(i)
for i in a:
	if i in b:
		c.append(i)
o=(l*r)//max(c)
print(o)
