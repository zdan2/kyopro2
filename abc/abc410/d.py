from collections import defaultdict,deque
n,m=map(int,input().split())
d=defaultdict(list)
m_c=0
for _ in range(m):
    a,b,w=map(int,input().split())
    d[a].append((b,w))
    m_c=1024
g=[[False]*(m_c+1) for _ in range(n+1)]
q=deque()
q.append((1,0))
while q:
    now,cur=q.popleft()
    for nxt,weight in d[now]:
        if not g[nxt][cur^weight]:
            g[nxt][cur^weight]=True
            q.append((nxt,cur^weight))
for i in range(m_c+1):
    if g[n][i]:
        print(i)
        break
else:
    print(-1)