def f(l,m,mid):
    box=1
    c=0
    for e in l:
        c+=e
        if c>mid:
            box+=1
            c=e
        if box>m:
            return False
        c+=1
    return True
n,m=map(int,input().split())
l=list(map(int,input().split()))
right=sum(l)+(n-1)
left=max(l)
mid=(left+right)//2
a=float('inf')
while left<=right:
    if f(l,m,mid):
        a=min(a,mid)
        right=mid-1
    else:
        left=mid+1
    mid=(left+right)//2
print(a)