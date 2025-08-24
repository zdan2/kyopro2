import heapq
hq=[]
q=int(input())
for _ in range(q):
    a=list(map(int,input().split()))
    if a[0]==1:
        heapq.heappush(hq,a[1])
    else:
        print(heapq.heappop(hq))