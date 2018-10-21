s = input()
i = 0
n = len(s)
a = []
b = []
while i<n :
    a.append(s[i])
    i += 1
    c = ''
    while i<n and s[i].isdigit()  :
        c = c + s[i]
        i += 1
    b.append(int(c))
c = ''
for i in range(0,len(a)) :
    c = c + a[i]*b[i]
print(c)
