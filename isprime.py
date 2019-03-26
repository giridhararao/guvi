import sys,string

def isPrime(n) :
    if n==1 : return False
    if n==2 or n==3 : return True
    for i in range(2,n) :
        if n%i == 0 :
            return False
    return True

a = int(input())
out = 0
for i in range(2,a//2+1) :
    if isPrime(i) and isPrime(a-i)  :
        out += 1
        
print(out)
