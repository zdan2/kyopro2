n,m=map(int,input().split())
a=list(map(int,input().split()))
d={}
for e in a:
    l=len(str(e))
    rem=e%m
    if rem not in d:
        d[rem]={}
    if l not in d[rem]:
        d[rem][l]=1
    else:
        d[rem][l]+=1
c=0
for x in a:
    for i in range(1,11):
        rem=(m-x*10**i%m)%m
        if rem in d and i in d[rem]:
            c+=d[rem][i]
print(c)