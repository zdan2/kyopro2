from atcoder import DSU
from collections import defaultdict
n,m=list(map(int,input().split()))
dsu=DSU(n)
d=defaultdict(list)
for _ in range(m):
  u,v=map(int,input().split())
  u-=1
  v-=1
  d[u].append(v)
  d[v].append(u)
  dsu.merge(u,v)
g=dsu.groups()
r=0
for e in g:
  c=0
  for k in e:
    c+=len(d[k])
  r+=(c//2-(len(e)-1))
print(r)