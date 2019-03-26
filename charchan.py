import sys,string, itertools

a = input()
n = len(a)
k = n//2
for j in range(n-1,-1,-1) :
    for i in range(0,n-j) :
        li, ri = i,j+i
        s1 = a[li:ri+1]
        for j in range(k,0,-1) :
            s21 = 'ab'*j
            s22 = s21 + 'a'
            if s22 in a :
                print(len(s22))
                sys.exit()
            elif s21 in a :
                print(len(s21))
                sys.exit()
print(0)
