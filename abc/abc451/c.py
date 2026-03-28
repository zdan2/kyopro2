import heapq
q=int(input())
hq=[]
for _ in range(q):
    a,b=map(int,input().split())
    if a==1:
        heapq.heappush(hq,b)
    else:
        while hq and hq[0]<=b:
            heapq.heappop(hq)
    print(len(hq))