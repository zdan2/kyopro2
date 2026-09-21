from collections import defaultdict
n,k=map(int,input().split())
d=defaultdict(int)
a=list(map(int,input().split()))
l=0
c=0
ans=0
for r in range(n):
    if d[a[r]]==0:
        c+=1
        d[a[r]]+=1
    while c>k:
        l+=1
        d[a[l]]-=1
        if d[a[l]]==0:
            c-=1
    ans=max(ans,r-l)
print(ans)    