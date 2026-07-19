n,m=map(int,input().split())
s=set()
t=set()
for _ in range(m):
    a,b=map(int,input().split())
    if min(a,b)==1:
        s.add(max(a,b))
    if max(a,b)==n:
        t.add(min(a,b))
print(['IMPOSSIBLE','POSSIBLE'][len(s&t)>0])