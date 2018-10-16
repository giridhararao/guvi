n=int(input())
a=input()
b=len(a)
z=[]
for i in range(1,b):
  z.append(a[-i])
z.append(a[0])
for i in z:
  if i=='a':
    z.remove(i)
  elif i=='e':
    z.remove(i)
  elif i=='i':
    z.remove(i)
  elif i=='o':
    z.remove(i)
  elif i=='u':
    z.remove(i)
out="".join(z)
print(out)
