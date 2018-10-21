def pri(n) :
    if n == 1 : return False
    if n == 2: return True
    for i in range(2,n) :
        if n%i == 0 : return False
    return True
def bina(i):
    if i == 0:
        return "0"
    s = ''
    while i:
        if i & 1 == 1:
            s = "1" + s
        else:
            s = "0" + s
        i //= 2
    return s

a,b = input().split()
a = int(a)
b = int(b)
o = 0
for i in range(a,b+1) :
    s = bina(i)
    k = s.count('1')
    if pri(k):
        o += 1
print(o)
