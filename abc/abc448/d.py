from collections import defaultdict,deque
n=int(input())
a=[0]+list(map(int,input().split()))
t=[False]*(n+1)
g=defaultdict(list)
g[0]=[1]
for _ in range(n-1):
    u,v=map(int,input().split())
    g[u].append(v)
    g[v].append(u)
q=deque([(0,{0})])
v=set()
while q:
    cur,path=q.popleft()
    if cur in v:
        continue
    v.add(cur)
    if not g[cur]:
        continue
    for ch in g[cur]:
        if ch in v:
            continue
        sf=path.copy()
        sf.add(a[ch])
        q.append((ch,sf))
        if t[cur]:
            t[ch]=True
        if a[ch] in path:
            t[ch]=True
for e in t[1:]:
    if e:
        print('Yes')
    else:
        print('No')