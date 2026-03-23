from collections import defaultdict
k=int(input())

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
    if k>1:
        d[k]=1
    return d

e=er(k)
r=f(k,e)

for i in range(2,20):
    d=f(i,e)
    for a,b in d.items():
        if a in r:
            r[a]-=b
            if r[a]<=0:
                del(r[a])
    if not r:
        print(i)
        exit()
c=1
for k,v in r.items():
    c*=k*v
print(c)