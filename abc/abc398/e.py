from collections import defaultdict,deque
n=int(input())
d=defaultdict(set)
for _ in range(n-1):
    u,v=map(int,input().split())
    d[u].add(v)
    d[v].add(u)
lv=[-1]*(n+1)
q=deque()
q.append((1,0))
while q:
    now,l=q.popleft()
    if lv[now]==-1:
        lv[now]=l
        for nxt in d[now]:
            q.append((nxt,(l+1)%2))
es=set()
os=set()
for i,e in enumerate(lv[1:]):
    if e==0:
        es.add(i+1)
    else:
        os.add(i+1)
lc=min(len(es),len(os))
used=set()
pm=set()
for i in es:
    for j in os:
        if j not in d[i]:
            pm.add((min(i,j),max(i,j)))
if len(pm)%2==1:
    print("First")
    h=0
else:
    print('Second')
    h=1
while True:
    if h==0:
        for (a,b) in pm:
            if (a,b) not in used:
                print(a,b)
                used.add((a,b))
                i,j=min(i,j),max(i,j)
                h=1
                break
    else:
        u,v=map(int,input().split())
        if u==-1:
            break
        pm.discard((u,v))
        used.add((u,v))
        h=0