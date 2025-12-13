import heapq
from collections import defaultdict
n=int(input())
pos=defaultdict(int)
can=defaultdict(bool)
rabit=defaultdict(set)
for i in range(n):
    x,r=map(int,input().split())
    left=x-r
    right=x+r
    pos[left]+=1
    pos[right]+=1
    can[left]=True
    can[right]=True
    rabit[left].add(i)
    rabit[right].add(i)
