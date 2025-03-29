from collections import defaultdict

def f(s,g,d,v=None):
    if v==None:
        v=set()
    if s not in v:
        v.add(s)
        for nxt in d[s]:
            if nxt==g:
                return 'Yes'
            r=f(nxt,g,d,v)
            if r=='Yes':
                return 'Yes'
    return 'No'
d=defaultdict(set)
n,q=map(int,input().split())
for _ in range(q):
    c,u,v=map(int,input().split())
    if c==1:
        if u not in d[v]:
            d[u].add(v)
            d[v].add(u)
        else:
            d[u].discard(v)
            d[v].discard(u)
    else:
        print(f(u,v,d))