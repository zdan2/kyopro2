from atcoder import DSU
n,m=map(int,input().split())
dsu=DSU(n*m)
mx=[list(input()) for _ in range(n)]
a,b,c,d=map(int,input().split())
for i in range(n):
    for j in range(m):
        if mx[i][j]=='.':
            for dy,dx in [[1,0],[-1,0],[0,1],[0,-1]]:
                ny=i+dy
                nx=j+dx
                if 0<=ny<n and 0<=nx<m and mx[i+dy][j+dx]=='.':
                    dsu.merge(i*m+j,ny*m+nx)
print(dsu.groups())