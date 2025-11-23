import heapq
n,k=map(int,input().split())
x=list(map(int,input().split()))+[float('inf')]
hq=[]
for i in range(k):
    heapq.heappush(hq,(-x[i],i+1))
for i in range(k,n+1):
    print(hq[0][1])
    if -hq[0][0]>x[i]:
        heapq.heappop(hq)
        heapq.heappush(hq,(-x[i],i+1))