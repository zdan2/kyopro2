import heapq
from collections import defaultdict
x=[]
y=[]
n=int(input())
pxy=defaultdict(list)
for i in range(n):
    a,b=map(int,input().split())
    x.append((a,i))
    y.append((b,i))
x.sort()
y.sort()
for i,e in enumerate(x):
    pxy[e[1]].append(i)
for i,e in enumerate(y):
    pxy[e[1]].append(i)
print(pxy)
print(x)
print(y)
used=[False]*n
dist=[float('inf')]