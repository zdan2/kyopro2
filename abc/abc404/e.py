from collections import defaultdict,deque
n=int(input())
c=[0]+list(map(int,input().split()))
a=[0]+list(map(int,input().split()))
d=defaultdict(list)
d[0]=[0]
for i,e in enumerate(c):
    for j in range(e):
        d[i].append(i-j-1)
route=[0]+[i for i in range(n) if a[i]==1]
route=route[::-1]
dist=[float('inf')]*n
dist[route[0]]=0

def bfs(s,g,dist):
    q=deque([s])
    while q:
        now=q.popleft()
        if now==g:
            return dist
        for nxt in d[now]:
            if dist[nxt]>dist[now]+1:
                dist[nxt]=dist[now]+1
                q.append(nxt)
s=route[0]
for g in route[1:]:
    r=bfs(s,g,dist)
    s=g
    dist=[float('inf')]*g+r[g:]
print(dist[0])