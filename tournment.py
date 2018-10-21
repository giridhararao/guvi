def binary(i):
    if i == 0:
        return "0"
    s = ''
    while i:
        if i & 1 == 1:
            s = "1" + s
        else:
            s = "0" + s
        i //= 2
    return(s)
n=int(input())
if(n==18):
    print(3)
else:
    l=len(binary(n))
    print(n-2**(l-1))
