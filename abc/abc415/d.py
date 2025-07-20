import heapq
n,m=map(int,input().split())
hq=[]
for _ in range(m):
    a,b=map(int,input().split())
    heapq.heappush(hq,(-b/a,a,b))
s=0
while hq:
    p,a,b=heapq.heappop(hq)
    if a<=n:
        n-=a
        n+=b
        s+=1
        heapq.heappush(hq,(p,a,b))
print(s)