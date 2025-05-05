n,l,t,x=map(int,input().split())
c=t
d=0
for _ in range(n):
    a,b=map(int,input().split())
    if b>=l:
        if a>t:
            print('forever')
            exit()
        elif a<c:
            c-=a
            d+=a
        elif a==c:
            d+=a+x
            c=t
        else:
            d+=c+x+a
            c=t-a
        if c==0:
            d+=x
            c=t
    else:
        d+=a
        c=t
print(d)