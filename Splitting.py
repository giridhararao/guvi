import sys, string, math

import sys,string
def dgtSum(n) :
    sum1 = 0
    while n :
        sum1 += n%10
        n //= 10
    return sum1

n = int(input())
A = []
cnt = 0
if n <= 5000 :
    for i in range(1,n) :
        if i + dgtSum(i) == n :
            cnt += 1
            A.append(i)
    print(cnt)
    print(*A)
else :
    for i in range(n-1000,n) :
        if i + dgtSum(i) == n :
            cnt += 1
            A.append(i)
    print(cnt)
    print(*L)
