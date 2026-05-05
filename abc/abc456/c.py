s=input()
a=[(0,0)]
b=[]
l=0
r=0
cur='*'
d=len(s)
mod=998244353
for i,e in enumerate(s):
    if e==cur:
        r=i
    else:
        if l!=r:
            n=l-a[-1][1]
            b.append((n*(n+1)//2)%mod)
            a.append((l,r))
        l=i
        r=i
        cur=e
if l!=r:
    n=l-a[-1][1]
    b.append((n*(n+1)//2)%mod)
    a.append((l,r))
n=len(s)-a[-1][1]-1
b.append((n*(n+1)//2)%mod)
print((d+sum(b))%mod)