from sortedcontainers import SortedList
from collections import defaultdict
n,k,m=map(int,input().split())
d=defaultdict(SortedList)
for _ in range(n):
    c,v=map(int,input().split())
    d[c].add(v)
a=SortedList()
for _,v in d.items():
    a.add(v.pop())
c=0
for _ in range(m):
    c+=a.pop()
for v in d.values():
    for e in v:
        a.add(e)
if k==m:
    print(c)
else:
    print(c+sum(a[-k+m:]))