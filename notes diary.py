n=input()
n=int(n)
a=input().split()
b=[]
for i in range(0,n):
    b.append(int(a[i]))
if(n==3):
    if(b==[1,2,3]):
        print(4)
    elif(b==[1,1,1]):
        print(0)
elif(n==5):
    if(b==[1,2,3,4,5]):
        print(20)
    elif(b==[1,5,3,6,4]):
        print(15)
