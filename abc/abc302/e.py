n,q=map(int,input().split())
d={i:set() for i in range(1,n+1)}

def connect(a,b):
    if (b,0) in d[a]:
        d[a].remove((b,0))
    d[a].add((b,1))

    for e,_ in d[a]:
        if (e,1) in d[b]:
            continue
        d[b].add((e,0))
        
def disconnect(a):
    for e,t in d[a]:
        

for _ in range(q):
    a=list(map(int,input().split()))
    if a[0]==1:
        u=a[1]
        v=a[2]
        connect(u,v)
        connect(v,u)
    else:
        disconnect(a[1])        
        