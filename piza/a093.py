from collections import deque
h,w,k=map(int,input().split())
mx=[list(map(int,input().split())) for _ in range(h)]
dyx=[(1,0),(0,1),(-1,0),(0,-1)]
mc=0
visited=[[False]*w for _ in range(h)]

def dfs(y,x,depth,c):
    global mc
    mc=max(mc,c)
    if depth==k:
        return
    visited[y][x]=True
    for dy,dx in dyx:
        ny=y+dy
        nx=x+dx
        if 0<=ny<h and 0<=nx<w and not visited[ny][nx]:
            dfs(ny,nx,depth+1,c+mx[ny][nx])
    visited[y][x]=False
for i in range(h):
    for j in range(w):
        dfs(i,j,0,mx[i][j])
    
print(mc)