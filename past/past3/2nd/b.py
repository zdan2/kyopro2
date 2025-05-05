from collections import defaultdict
n,m,q=map(int,input().split())
s=defaultdict(int)
c=defaultdict(set)
for _ in range(q):
    x=list(map(int,input().split()))
    if x[0]==1:
        a=0
        for v in c[x[1]]:
            a+=n-s[v]
        print(a)
    if x[0]==2:
        c[x[1]].add(x[2])
        s[x[2]]+=1