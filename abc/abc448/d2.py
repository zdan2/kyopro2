import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)
n=int(input())
a=list(map(int,input().split()))
d=defaultdict(list)
for _ in range(n-1):
    u,v=map(int,input().split())
    d[u].append(v)
    d[v].append(u)
ans=[False]*n
cnt=defaultdict(int)
parent=[False]*n
def dfs(v, p):
    if cnt[a[v-1]] > 0 or parent[p-1]:
        ans[v-1] = True
        parent[v-1]=True
    cnt[a[v-1]] += 1
    for nv in d[v]:
        if nv==p:
            continue
        dfs(nv,v)
    cnt[a[v-1]] -= 1

dfs(1,0)

for x in ans:
    print("Yes" if x else "No")