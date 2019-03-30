a = input()
for i in range(11,100,11) :
    a2 = str(i)
    if a2 in a :
        i2 = a.index(s2)
        a3 = a[:i2] + a2[0] + a[i2+2:]
        print(a3)
        break
