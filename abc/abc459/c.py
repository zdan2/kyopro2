from collections import defaultdict
n,q=map(int,input().split())
bk=[0]*(n+1)
th=0
d=defaultdict(int)
for _ in range(q):
    a,b=map(int,input().split())
    if a==1:
        bk[b]+=1
        d[bk[b]]+=1
        if d[bk[b]]==n:
            th+=1
    else:
        print(d[b+th])