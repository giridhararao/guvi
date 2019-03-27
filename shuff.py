import sys,string
a = input()
b = len(a)
c = list(a)
c.sort(key = lambda x : c.count(x))
if len(c) - c.count(c[0]) >= c.count(c[0])-1 :
    print('yes')
else :
    print('no')
