import sys, string, math
def ditsum(n) :
    sum1 = 0
    while n :
        sum1 += n%10
        n //= 10
    return sum1
n = int(input())
o = []
cnt = 0
if(n <= 5000):
    for i in range(1,n) :
        if(i + ditsum(i) == n):
            cnt += 1
            o.append(i)
    print(cnt)
    print(*o)
else :
    for i in range(n-1000,n) :
        if(i + ditsum(i) == n):
            cnt += 1
            o.append(i)
    print(cnt)
    print(*o)
