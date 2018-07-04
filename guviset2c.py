a=int(input())
c=0
for b in range(2,a//2+1):
   if(a%b==0):
     c=c+1
if(c<=0 or a=2):
  print("Yes")
else:
  print("No")
