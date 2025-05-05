from collections import defaultdict
from itertools import product
n,m=map(int,input().split())
r=[[] for _ in range(n)]
c=list(map(int,input().split()))
for i in range(m):
    k=list(map(int,input().split()))
    for e in k[1:]:
        r[e-1].append(i+1)
mc=float('inf')
for i in product([0,1,2],repeat=n):
    d=defaultdict(int)
    cost=0
    for j in range(n):
        cost+=c[j]*i[j]
        for e in r[j]:
            d[e]+=i[j]
    animal=min(d.values())
    if len(d)==m and animal>=2:
        mc=min(mc,cost)
print(mc)