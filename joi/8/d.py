w=int(input())
h=int(input())
mx=[list(map(int,input().split())) for _ in range(h)]
visited=set()
dyx=[(1,0),(0,1),(-1,0),(0,-1)]
def f(y,x):
    maxdepth=0
    visited.add((y,x))
    for dy,dx in dyx:
        ny=y+dy
        nx=x+dx
        if 0<=ny<h and 0<=nx<w and (ny,nx) and mx[ny][nx]==1 and (ny,nx) not in visited:
            maxdepth=max(maxdepth,f(ny,nx))
    visited.remove((y,x))
    return maxdepth+1
mc=0
for i in range(h):
    for j in range(w):
        if mx[i][j]==1:
            r=f(i,j)
            mc=max(mc,r)
print(mc)