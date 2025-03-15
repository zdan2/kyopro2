from collections import defaultdict
n,m,q=map(int,input().split())
score_m=[n]*(m+1)
d=defaultdict(list)
for _ in range(q):
    query=list(map(int,input().split()))
    if query[0]==1:
        c=0
        for e in d[query[1]]:
            c+=score_m[e]
        print(c)
    if query[0]==2:
        d[query[1]].append(query[2])
        score_m[query[2]]-=1
        