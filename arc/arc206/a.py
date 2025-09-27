from collections import  defaultdict
n=int(input())
a=list(map(int,input().split()))
c=defaultdict(int)
r=1
for l in range(n-1,-1,-1):
    e=n-l
    c[a[l]]+=1
    f=l==0 or a[l]!=a[l-1]
    if f:
        r+=e-c[a[l]]
print(r)