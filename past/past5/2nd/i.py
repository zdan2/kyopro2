from collections import defaultdict,deque
n,m,k=map(int,input().split())
h=list(map(int,input().split()))
c=set(map(int,input().split()))
d=defaultdict(list)
for _ in range(m):
    a,b=map(int,input().split())
    a-=1
    b-=1
    if h[a]<h[b]:
        d[a].append(b)
    else:
        d[b].append(a)
q=deque()
r=[float('inf')]*n
for e in c:
    e-=1
    q.append((e))
    r[e]=0
v=set()
while q:
    now=q.popleft()
    for nxt in d[now]:
        if r[nxt]>r[now]+1:
            r[nxt]=r[now]+1
            q.append(nxt)
for e in r:
    if e==float('inf'):
        print(-1)
    else:
        print(e)