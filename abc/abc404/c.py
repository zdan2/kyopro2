from collections import defaultdict
n,m=map(int,input().split())
d=defaultdict(list)
for _ in range(m):
    a,b=map(int,input().split())
    d[a].append(b)
    d[b].append(a)
for e in d.values():
    if len(e)!=2:
        print('No')
        exit()
v=set()
s=[1]
while s:
    now=s.pop()
    if now not in v:
        v.add(now)
        for nxt in d[now]:
            s.append(nxt)
if n==m and len(v)==n:
    print('Yes')
else:
    print('No')