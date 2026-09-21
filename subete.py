from collections import defaultdict
from sortedcontainers import SortedSet
n,m=map(int,input().split())
jobs=[0]*n
a=list(map(int,input().split()))
d=defaultdict(list)
for _ in range(m):
    u,v=map(int,input().split())
    u-=1
    v-=1
    jobs[v]+=1
    d[u].append(v)
hq=SortedSet()
time=[float('inf')]*n
for u,w in enumerate(jobs):
    if w==0:
        hq.add((a[u],u))
        time[u]=a[u]
while hq:
    cur,job=hq.pop(0)
    for nxt in d[job]:
        jobs[nxt]-=1
        if jobs[nxt]==0:
            if time[nxt]>cur+a[nxt]:
                time[nxt]=cur+a[nxt]
                hq.add((cur+a[nxt],nxt))
print(max(time))