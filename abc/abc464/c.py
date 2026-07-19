from collections import defaultdict
n,m=map(int,input().split())
cur=[0]*(n+1)
di=defaultdict(dict)
do=defaultdict(dict)
s=set()
for _ in range(n):
    a,d,b=map(int,input().split())
    if b not in di[d]:
        di[d][b]=1
    else:
        di[d][b]+=1
    if a not in do[d]:
        do[d][a]=1
    else:
        do[d][a]+=1
    cur[a]+=1
    s.add(a)
c=len(s)
for day in range(1,m+1):
    for k,v in do[day].items():
        cur[k]-=v
        if cur[k]==0:
            c-=1
    for k,v in di[day].items():
        if cur[k]==0:
            c+=1
        cur[k]+=v
    print(c)