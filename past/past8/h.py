from collections import defaultdict,deque

def bsf(start,tree):
    visited=set()
    cost=[]
    q=deque([(start,[0])])
    while q:
        now,nowc=q.popleft()
        if now not in visited:
            visited.add(now)
            cost.append(nowc)
            for nxt,nxtc in tree[now]:
                q.append((nxt,nowc+[nowc[-1]+nxtc]))
    return cost
        
    
    
n,x=map(int,input().split())
d=defaultdict(list)

for _ in range(n-1):
    a,b,c=map(int,input().split())
    d[a].append((b,c))
    d[b].append((a,c))
    
can=[]
for node,edges in d.items():
    if len(edges)==1:
        can.append(node)
        
for e in can:
    print(e,bsf(e,d))

            
        