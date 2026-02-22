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
    x=[]
    for i in range(len(r)):
        c=1
        for k,v in lcm.items():
            if k in r[i]:
                if r[i][k]==v[1]:
                    for _ in range(v[0]):
                        c*=k
                        c%=mod
                else:
                    for _ in range(v[1]):
                        c*=k
                        c%=mod
            else:
                for _ in range(v[1]):
                    c*=k
                    c%=mod
        x.append(c)
    print(*x)