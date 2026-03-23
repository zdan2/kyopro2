from sortedcontainers import SortedSet
from collections import Counter
n,q=map(int,input().split())
a=list(map(int,input().split()))
s=SortedSet(a)
c=Counter(a)
def f_mex(s):
    l=0
    r=len(s)
    while l<r:
        mid=(l+r)//2
        if s[mid]==mid:
            l=mid+1
        else:
            r=mid
    return  r
for _ in range(q):
    idx,b=map(int,input().split())
    idx-=1
    c[a[idx]]-=1
    if c[a[idx]]==0:
        s.remove(a[idx])
    s.add(b)
    if b in c:
        c[b]+=1
    else:
        c[b]=1
    a[idx]=b
    
    print(f_mex(s))