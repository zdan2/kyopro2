n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]
y=-1
x=-1
for i in range(n):
    for j in range(n):
        if a[i][j]==0:
            y=i
            x=j
c=0
for v in range(1,n+1):
    a[y][x]=v
    h=True
    for k in range(n):
        if a[v-1][k]!=a[y][a[x][k]-1]:
            h=False
            break
    if h:
        print(v)
        c+=1
print(c)