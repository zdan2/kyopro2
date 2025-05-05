from collections import defaultdict
n,k=map(int,input().split())
c=list(map(int,input().split()))
p=list(map(int,input().split()))
d=defaultdict(lambda:float('inf'))
for a,b in zip(c,p):
    d[a]=min(d[a],b)
if len(d)<k:
    print(-1)
else:
    print(sum(sorted([v for v in d.values()])[:k]))