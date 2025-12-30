import heapq
n=int(input())
a=[tuple(map(int,input().split())) for _ in range(n)]
hq=[]
for t,d in a:
    heapq.heappush(hq,(t,t+d))
c=0
cur=1
while hq:
    if hq[0]<=cur:
        inn,out=heapq.heappop(hq)
        if inn<=cur and out>=cur:
            c+=1
            cur+=1

        
