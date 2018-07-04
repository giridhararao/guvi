a=int(input())
b=int(input())
for c in range((a+1),b):
    f=0
    for e in range(2,c//2+1):
       if(c%e==0):
         f=f+1
    if(f>0):
      print(c)
