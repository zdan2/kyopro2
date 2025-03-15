from collections import defaultdict

n,k=map(int,input().split())
c=list(map(int,input().split()))
p=list(map(int,input().split()))
d=defaultdict(lambda:float('inf'))

for co,pr in zip(c,p):
    d[co]=min(d[co],pr)

sd =sorted([v for k,v in d.items()])

if len(sd)>=k:
    print(sum(sd[:k]))
else:
    print(-1)