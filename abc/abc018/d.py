n,m,p,q,r=map(int,input().split())
x=[tuple(map(int,input().split())) for _ in range(r)]
mc=0
for i in range(2**n):
    if i.bit_count()!=p:
        continue
    c=[0]*m
    for g,b,h in x:
        g-=1
        b-=1
        if i>>g&1:
            c[b]+=h
    c.sort()
    mc=max(mc,sum(c[-q:]))
print(mc)