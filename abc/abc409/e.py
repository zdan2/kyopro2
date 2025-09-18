from collections import defaultdict,deque
n=int(input())
x=[0]+list(map(int,input().split()))
d=defaultdict(list)
for _ in range(n-1):
    u,v,w =map(int,input().split())
    d[u].append([v,w])
    d[v].append([u,w])
q=deque([1])
visited=set()
l=[0]*(n+1)
p=[0]*(n+1)
while q:
    now=q.popleft()
    if now not in visited:
        visited.add(now)
        for nxt,_ in d[now]: 
            if nxt in visited:
                continue
            p[nxt]=now
            l[nxt]=l[now]+1
            q.append(nxt)
lc=sorted([(e,i) for i,e in enumerate(l)])
te=0
while lc:
    _,now=lc.pop()
    parent=p[now]
    for nxt,cost in d[now]:
        if nxt==parent:
            te+=cost*abs(x[now])
            x[parent]+=x[now]
print(te)