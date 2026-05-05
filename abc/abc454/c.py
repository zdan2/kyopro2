import sys
sys.setrecursionlimit(10**7)
from collections import defaultdict
n,m=map(int,input().split())
d=defaultdict(list)
for _ in range(m):
    a,b=map(int,input().split())
    d[a].append(b)
v=set()
v.add(1)
def dfs(a):
    if a not in d:
        return
    for nxt in d[a]:
        if nxt not in v:
            v.add(nxt)
            dfs(nxt)
dfs(1)
print(len(v))