from collections import defaultdict, deque
n,m=map(int,input().split())
d=defaultdict(list)
for _ in range(m):
    a,b,x,y=map(int,input().split())
    d[a].append((b,(x,y)))
    d[b].append((a,(-x,-y)))
r=[-1]*(n+1)
q=deque()
q.append((1,(0,0)))
while q:
    p,xy=q.popleft()
    x,y=xy
    if r[p]==-1:
        r[p]=xy
        for np,nxy in d[p]:
            nx,ny=nxy
            nx+=x
            ny+=y
            q.append((np,(nx,ny)))
for e in r[1:]:
    if e==-1:
        print('undecidable')
    else:
        print(*e)