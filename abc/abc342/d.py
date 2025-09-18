from collections import defaultdict
m=int(input())
a=list(map(int,input().split()))
spf=[0]*(max(a)+1)
spf[1]=1
for i in range(2,max(a)+1):
    if spf[i]==0:
        spf[i]=i
        for j in range(i*i,max(a)+1,i):
            if spf[j]==0:
                spf[j]=i

r=[]
for e in a:
    f=defaultdict(int)
    p=spf[e]
    n=e
    if n==0:
        r.append(0)
        continue
    if n==1:
        r.append(1)
        continue
    while n>1:
        p=spf[n]
        while spf[n]==p:
            n//=p
            f[p]^=1
    odp=frozenset(k for k,v in f.items() if v==1)
    r.append(odp)
#print(r)
c=defaultdict(int)
one=m-len(r)
for p in r:
    c[p]+=1
#print(c)
a=0
for e,g in c.items():
    if e==0:
        a+=g*m-(g+1)*g//2
    elif e==1:
        a+=g*one-(g+1)*g//2
    else:
        a+=g*(g-1)//2
print(a)  