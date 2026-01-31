from itertools import combinations_with_replacement
n,m,q=map(int,input().split())
r=[]
for seq in combinations_with_replacement(range(1,m+1),n):
    r.append(list(seq))
q=[tuple(map(int,input().split())) for _ in range(q)]
ans=0
for e in r:
    h=0
    for a,b,c,d in q:
        a-=1
        b-=1
        if e[b]-e[a]==c:
            h+=d
    ans=max(ans,h)
print(ans)         