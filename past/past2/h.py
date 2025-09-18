from collections import defaultdict
n,m=map(int,input().split())
d=defaultdict(list)
mx=[list(input()) for _ in range(n)]
for i in range(n):
    for j in range(m):
        if mx[i][j]=='S':
            d[0].append((i,j))
        elif mx[i][j]=='G':
            d[10].append((i,j))
        else:
            d[int(mx[i][j])].append((i,j))
stack=[(d[0][0],d[0][1],0)]
for i in range(1,11):
    for ny,nx in d[i+1]:
        r=float('inf')
        for y,x in d[i]:
            
