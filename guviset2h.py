g=int(input())
h=int(input())
s1=list()
x=0
y=0
for a in range((g+1),h)
 ref=a
 ref1=a
 while(a>0):
   a=a//10
   x=x+1
 for i in range(x):
   s1[i]=ref1%10
   ref1=ref1//10
 for j in s1:
   y=y+(j**x)
 if(ref==y):
   print(ref)
