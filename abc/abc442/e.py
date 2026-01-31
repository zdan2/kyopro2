from math import atan2,pi
from bisect import bisect,bisect_left
n,q=map(int,input().split())
d={}
r=[]
for i in range(n):
   x,y=map(int,input().split())
   a=pi+atan2(y,x)*-1
   d[i+1]=a
   a=pi+atan2(y,x)*-1
   r.append(a)
   r.append(a+pi*2)
r.sort()
for _ in range(q):
    u,v=map(int,input().split())
    if d[u]>d[v]:
        left=d[u]
        right=d[v]+2*pi
    elif d[u]==d[v]:
        left=d[u]-(10**(-12))
        right=d[v]+(10**(-12))
    else:
        left=d[u]
        right=d[v]
    lidx=bisect_left(r,left)
    ridx=bisect(r,right)
    print(ridx-lidx)