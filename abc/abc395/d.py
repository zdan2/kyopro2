n,q=map(int,input().split())
pi=[i+1 for i in range(n)]
ne={i+1:i+1 for i in range(n)}
nei=
for _ in range(q):
    op,a,*r=map(int,input().split())
    if op==1:
        b=r[0]
        pi[a-1]=b
    if op==2:
        b=r[0]
        ne[a],ne[b]=ne[b],ne[a]
    if op==3:
        print(ne[pi[a-1]])