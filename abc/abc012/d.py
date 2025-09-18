n=int(input())
d=[list(map(int,input().split())) for _ in range(n)]
dc=[]
for r in d:
    dc.append(r[:])
h=[[True]*n for _ in range(n)]
for i in range(n):
    h[i][i]=False
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i==k or k==j:
                continue
            if d[i][j]==d[i][k]+d[k][j]:
                h[i][j]=False
            elif d[i][j]>d[i][k]+d[k][j]:
                d[i][j]=d[i][k]+d[k][j]
if d!=dc:
    print(-1)
    exit()
c=0
for i in range(n-1):
    for j in range(i+1,n):
        if h[i][j]:
            c+=d[i][j]
print(c)