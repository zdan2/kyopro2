def er(n):
    srn=int(n**0.5)+1
    t=[True]*srn
    t[0]=False
    t[1]=False
    for i in range(srn):
        if t[i]==False:
            continue
        for j in range(i+i,srn,i):
            t[j]=False    
    p=[i for i,v in enumerate(t) if v]
    return p
def f(n,pl):
    d={}
    a=n
    for i in range(len(pl)):
        if a and a%pl[i]==0:
            d[pl[i]]=0
            while a and a%pl[i]==0:
                a//=pl[i]
                d[pl[i]]+=1
        if pl[i]*pl[i]>a:
            break
    if a>1:
        d[a]=1
    return d
mod=998244353
t=int(input())
q=[[int(input()),list(map(int,input().split()))] for _ in range(t)]
n=max(max(v[1]) for v in q)
pl=er(n)
for k,l in q:
    r=[]
    lcm={}
    for e in l:
        b=f(e,pl)
        r.append(b)
        for k,v in b.items():
            if k not in lcm:
                lcm[k]=[0,v]
            else:
                if v>=lcm[k][1]:
                    lcm[k].pop(0)
                    lcm[k].append(v)
                elif v>lcm[k][0]:
                    lcm[k][0]=v
    LCM=1
    for k,v in lcm.items():
        LCM=(LCM*pow(k,v[1],mod))%mod
    x=[]
    for d in r:
        a=LCM
        for k,v in d.items():
            if lcm[k][1]==v:
                a=a*pow(pow(k,lcm[k][1]-lcm[k][0],mod),mod-2,mod)%mod
        x.append(a)
    print(*x)