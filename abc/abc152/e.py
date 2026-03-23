from collections import defaultdict
def er(n):
    sqrt=int(n**0.5)+1
    f=[True]*sqrt
    f[0]=False
    f[1]=False
    for i in range(2,sqrt):
        if f[i]:
            for j in range(i+i,sqrt,i):
                f[j]=False
    return f
def f(k,er):
    d=defaultdict(int)
    f=er
    for i,e in enumerate(f):
        if e:
            while k%i==0:
                d[i]+=1
                k//=i
            if k==1:
                return d
    if k>1:
        d[k]=1
    return d
mod=10**9+7
n=int(input())
a=list(map(int,input().split()))
e=er(max(a))
r={}
b=[]
for m in a:
    g=f(m,e)
    b.append(g)
    for k,v in g.items():
        if k not in r:
            r[k]=v
        else:
            r[k]=max(r[k],v)
ans=0
for h in b:
    c=1
    for k,v in r.items():
        if k in h:
            if v==h[k]:
                v=0
            else:
                v=max(v,h[k])-min(v,h[k])
        c=(c*pow(k,v,mod))%mod    
    ans=(ans+c)%mod
print(ans)