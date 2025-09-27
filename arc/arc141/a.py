def ff(s):
    l=len(s)
    h=l//2
    res=10**(l-1)-1
    for i in range(1,h+1):
        f=s[:i]
        can=f*(l//i)
        if can>s:
            d=max(0,int(f)-1)
            d=str(d)
            can=d*(l//i)
        res=max(res,int(can))
    return res
t=int(input())
for _ in range(t):
    print(ff(input()))