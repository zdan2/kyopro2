from bisect import bisect
n,k,l,m=map(int,input().split())
d=list(map(int,input().split()))
left=d[0]
right=left+l
lidx=0
ridx=bisect(d,right)
r=min(m,ridx)
for i in range(r):
    