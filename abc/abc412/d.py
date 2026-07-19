from itertools import permutations
n,m=map(int,input().split())
e=set()
for _ in range(m):
    u,v=map(int,input().split())
    e.add((min(u,v),max(u,v)))

def c(p):
    t=set()
    for i in range(n):
        a,b=i+1,p[i]
        if a==b:
            return None
        if p[b-1]==a:
            return None
        t.add((min(a,b),max(a,b)))
    return len(e-t)+len(t-e)
        
r=float('inf')
for p in permutations(range(1,n+1)):
    f=c(p)
    if f is not None:
        r=min(r,f)
print(r)