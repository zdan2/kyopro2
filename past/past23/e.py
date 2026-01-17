import heapq
from math import lcm
n=int(input())
hq=[]
x=[]
l=1
for i in range(n):
    a,b=map(int,input().split())
    x.append((a,b))
    l=lcm(l,b)
for i,(a,b) in enumerate(x):
    heapq.heappush(hq,(a*l//b,i))
while hq:
    _,i =heapq.heappop(hq)
    print(*x[i])