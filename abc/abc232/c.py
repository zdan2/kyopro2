from itertools import permutations
n,m=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(m)]
a.sort()
b=[list(map(int,input().split())) for _ in range(m)]
b.sort()
if a==b:
    print('Yes')
    exit()
for p in permutations(range(1,n+1),n):
    c=[]
    for u,v in b:
        c.append(sorted([p[u-1],p[v-1]]))
    c.sort()
    if a==c:
        print('Yes')
        exit()
print('No')
    