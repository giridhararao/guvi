import sys,string
def jumpnum(n) :
    s = str(n)
    a = len(s)
    for i in range(0,a-1) :
        if abs(int(s[i]) - int(s[i+1])) != 1 :
            return False
    return True

n = int(input())
if n <= 9 :
    print(n+1)
    sys.exit()
out = 10
for i in range(10,n+1) :
    if jumpnum(i) :
        out += 1

print(out)
