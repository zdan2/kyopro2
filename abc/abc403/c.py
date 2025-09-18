from collections import defaultdict
n,m,q=map(int,input().split())
d=defaultdict(set)
for _ in range(q):
    x=list(map(int,input().split()))
    if x[0]==1:
        d[x[1]].add(x[2])
    if x[0]==2:
        d[x[1]].add(0)
    if x[0]==3:
        if 0 in d[x[1]] or x[2] in d[x[1]]:
            print('Yes')
        else:
            print('No')