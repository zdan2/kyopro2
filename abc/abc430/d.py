from collections import defaultdict
from sortedcontainers import SortedList
n=int(input())
x=list(map(int,input().split()))
r=SortedList([0])
d=defaultdict(list)
d[0]=[float('inf'),0]
c=0
for e in x:
    idx=r.bisect(e)
    if 0<idx<len(r):
        print('r',r[idx-1],r[idx])
        o_l=d[r[idx-1]][1]
        o_r=d[r[idx]][0]
        d_l=e-r[idx-1]
        d_r=r[idx]-e
        d[r[idx-1]][1]=d_l
        d[r[idx]][0]=d_r
        d[e]=[d_l,d_r]
        c-=o_l
        c-=o_r
        c+=min(d[r[idx-1]])
        c+=min(d[r[idx]])
        c+=min(d_l,d_r)
    else:
        c-=min(d[r[-1]])
        d[r[-1]][1]=e-r[-1]
        c+=e-r[-1]
        c+=min(d[r[-1]])
        d[e]=[e-r[-1],float('inf')]
    r.add(e)
    print('c',c)
print(d)
        
