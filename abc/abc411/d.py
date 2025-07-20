from collections import defaultdict
d=defaultdict(list)
n,q=map(int,input().split())
pa=list(range(n+1))
for _ in range(q):
    p=list(input().split())
    p[0],p[1]=int(p[0]),int(p[1])
    if p[0]==1:
        pa[p[1]]=0
    if p[0]==2:
        d[p[1]].append(p[2])
    if p[0]==3:
        pa[0]=pa[p[1]]
print(d)