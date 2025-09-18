import math
n,m,k=map(int,input().split())
l=0
r=10**18
can=None
while l<r:
    mid=(l+r)//2
    dn=mid//n
    dm=mid//m
    dnm=mid//(math.lcm(n,m))
    a=dn+dm-2*dnm
    if a<k:
        l=mid+1
    else:
        r=mid
    if a==k and ((mid % n != 0 and mid % m == 0) or (mid % n == 0 and mid % m != 0)):
        can = mid if can is None else min(can, mid)
print(can)