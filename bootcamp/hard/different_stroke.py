import heapq
from collections import defaultdict
n=int(input())
hqt=[]
hqa=[]
eated=defaultdict(int)
for _ in range(n):
    a,b=map(int,input().split())
    heapq.heappush(hqt,(-a,-b))
    heapq.heappush(hqa,(-b,-a))
    eated[(a,b)]+=1
tc=0
ac=0
while hqt or hqa:
    while hqt:
        ta,at=heapq.heappop(hqt)
        if eated[(-ta,-at)]> 0:
            eated[(-ta,-at)]-=1
            tc-=ta
            break
    while hqa:
        at,ta=heapq.heappop(hqa)
        if eated[(-ta,-at)]>0:
            eated[(-ta,-at)]-=1
            ac-=at
            break
print(tc-ac)