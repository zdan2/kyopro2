import heapq
n,m=map(int,input().split())
hq=[]
for _ in range(m):
    a,b=map(int,input().split())
    heapq.heappush(hq,(a-b,a,b))
s=0
while hq:
    d,a,b=heapq.heappop(hq)
    if a<=n:
        k=max(0, (n-a)//(a-b)+1)
        n-=k*(a-b)
        s+=k
print(s)