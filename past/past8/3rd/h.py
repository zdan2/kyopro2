from collections import deque
n,x=map(int,input().split())
parent=[i for i in range(n+1)]
child=[{i} for i in range(n+1)]
dist=[0 for _ in range(n+1)]
town={}
visited=set()
for _ in range(n-1):
    a,b,c=map(int,input().split())
    if a not in town:
        town[a]=[(b,c)]
    else:
        town[a].append((b,c))
    if b not in town:
        town[b]=[(a,c)]
    else:
        town[b].append((a,c))
q=deque([1])
while q:
    now=q.popleft()
    visited.add(now)
    for nxt,c in town[now]:
        if nxt not in visited:
            visited.add(nxt)
            q.append(nxt)
            parent[nxt]=now
            p=now
            while True:
                child[p].add(nxt)
                if p==parent[p]:
                    break
                else:
                    p=parent[p]
            dist[nxt]+=dist[now]+c
for i in range(1,n):
    for j in range(i+1,n+1):
        now=j
        while True:
            if i in child[now]:
                r=dist[i]+dist[j]-dist[now]*2
                break
            else:
                now=parent[now]
        if r==x:
            print('Yes')
            exit()
print('No')