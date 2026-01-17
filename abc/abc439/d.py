from collections import defaultdict
n=int(input())
a=list(map(int,input().split()))
d=defaultdict(int)
c=0
for i in range(n):
    ai=a[i]*115//35
    ak=a[i]*115//15
    if ai in d and ak in d:
        c+=d[ai]*d[ak]
    d[a[i]*115//21]+=1
d=defaultdict(int)
for i in range(n-1,-1,-1):
    ai=a[i]*115//35
    ak=a[i]*115//15
    if ai in d and ak in d:
        c+=d[ai]*d[ak]
    d[a[i]*115//21]+=1
print(c)