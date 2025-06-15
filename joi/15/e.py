from collections import deque,defaultdict
import heapq
n,m,k,s=map(int,input().split())
p,q=map(int,input().split())
zom={int(input()) for _ in range(k)}
d=defaultdict(list)
for _ in range(m):
    a,b=map(int,input().split())
    d[a].append(b)
    d[b].append(a)
da_vil=[False]*(n+1)
dq_dvil=deque()
for v in zom:
    dq_dvil.append((v,0))
while dq_dvil:
    now,dist=dq_dvil.popleft()
    da_vil[now]=True
    for nxt in d[now]:
        if dist+1<=s and not da_vil[nxt]:
            da_vil[nxt]=True
            dq_dvil.append((nxt,dist+1))
da_vil=set([i for i,e in enumerate(da_vil) if e])^zom
dq_trip=[]
heapq.heappush(dq_trip,(0,1))
hotel=[float('inf')]*(n+1)
hotel[1]=0
while dq_trip:
    spend,now=heapq.heappop(dq_trip)
    for nxt in d[now]:
        if nxt in zom:
            continue
        if nxt in da_vil:
            if hotel[nxt]>spend+q:
                hotel[nxt]=spend+q
                heapq.heappush(dq_trip,(spend+q,nxt))
        else:
            if hotel[nxt]>spend+p:
                hotel[nxt]=spend+p
                heapq.heappush(dq_trip,(spend+p,nxt))
cheap=float('inf')
for pre in d[n]:
    cheap=min(cheap,hotel[pre])
print(cheap)