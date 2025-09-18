from collections import defaultdict
h,w,n=map(int,input().split())
dh=defaultdict(set)
dw=defaultdict(set)
for _ in range(n):
    x,y=map(int,input().split())
    dh[x].add(y)
    dw[y].add(x)
q=int(input())
for _ in range(q):
    x,y=map(int,input().split())
    if x==1:
        print(len(dh[y]))
        for e in dh[y]:
            dw[e].discard(y)
        dh[y]={}
    if x==2:
        print(len(dw[y]))
        for e in dw[y]:
            dh[e].discard(y)
        dw[y]={}