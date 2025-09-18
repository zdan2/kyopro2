import heapq

n,m,k,q=map(int,input().split())

hq0=[]
hq1=[]

for _ in range(n):
    p,t=map(int,input().split())
    if t==0:
        heapq.heappush(hq0,p)
    else:
        heapq.heappush(hq1,p)

count=0
cost=0
kc=0
for _ in range(m):
    if hq0:
        can0=heapq.heappop(hq0)
    else:
        can0=float('inf')
    if hq1:
        can1=heapq.heappop(hq1)
    else:
        can1=float('inf')
            
    if kc==0:
        can1+=q
        
    if can0<can1:
        cost+=can0
        if kc==0:
            can1-=q
            heapq.heappush(hq1,can1)
    else:
        cost+=can1
        heapq.heappush(hq0,can0)
        if kc==0:
            kc=k-1
        else:
            kc-=1
print(cost)
    