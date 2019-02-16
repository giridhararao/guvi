import sys
a = input()
if a == a[::-1] :
    print('yes')
    sys.exit()
k = 0
for c in a[::-1] :
    if c == '0' :
        k += 1
    else :
        break
b = '0'*k + a
if b == b[::-1] :
    print('yes')
else :
    print('no')
