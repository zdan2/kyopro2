from collections import defaultdict
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    d=defaultdict(set)
    top=float('inf')
    for i in range(n):
        if i-1>=0:
            d[a[i]].add(i-1)
        if i+1<n:
            d[a[i]].add(i+1)
        top=min(top,a[i])
    cur=top
    v=set()
    count=0
    while len(v)<n:
        for idx in d[cur]:
            if idx in v:
                continue
            if a[idx]<=cur:
                v.add(idx)
                continue
            v.add(idx)
            b=a[idx]
            count+=b-cur-1
            a[idx]=min(b,cur+1)
            if idx-1>=0:
                d[cur+1].add(idx-1)
            if idx+1<n:
                d[cur+1].add(idx+1)
        cur+=1
    print(count)