n=int(input())
x=list(map(int,input().split()))
mx=max(x)
er=[True]*(mx+1)
er[0]=False
er[1]=False
for i in range(2,mx+1):
    if er[i]:
        j=2
        while j*i<=mx:
           er[j*i]=False
           j+=1
p=[]
for i in range(mx+1):
    if er[i]:
        p.append(i)
ans=float('inf')
for i in range(2**len(p)):
    can=[]
    res=1
    for j in range(len(p)):
        if (i>>j)&1:
            can.append(p[j])
    f=set()
    for e in x:
        for k in can:
            if e%k==0:
                f.add(k)
                break
        else:
            f.add(e)
    for l in f:
        res*=l
    ans=min(ans,res)
print(ans) 