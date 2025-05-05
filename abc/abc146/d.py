from collections import defaultdict,deque
r=[]
q=[]
d=defaultdict(list)
n=int(input())
for _ in range(n-1):
    a,b=map(int,input().split()) 
    a,b=min(a,b),max(a,b)
    d[a].append(b)
    d[b].append(a)
    r.append((a,b))
mc=max(len(e) for e in d.values())
q=deque()
q.append((1,0))
v=set()
c=defaultdict(int)
while q:
    now,nc=q.popleft()
    co=0
    if now not in v:
        v.add(now)
        for ne in d[now]:
            if nc==co:
                co+=1
            if not c[(min(now,ne),max(now,ne))]:
                c[(now,ne)]=co
                q.append((ne,co))
            co+=1
print(c)
for p in r:
    print(c[p]) 