import heapq
a,b,c,n=map(int,input().split())
hq=[1]
v=set()
for i in range(n-1):
    k=heapq.heappop(hq)
    for e in [a,b,c]:
        if k*e not in v:
            v.add(k*e)
            heapq.heappush(hq,k*e)
print(hq[0])