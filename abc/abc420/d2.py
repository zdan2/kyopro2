from collections import deque

h,w=map(int,input().split())
mx=[list(input()) for _ in range(h)]
dq=deque()
visited=[set(),set()]
dyx=[(1,0),(0,1),(-1,0),(0,-1)]
door=['x','o']
f=0
sy,sx,gy,gx = 0, 0, 0, 0
for i in range(h):
    for j in range(w):
        if mx[i][j]=='S':
            sy=i
            sx=j
        if mx[i][j]=='G':
            gy=i
            gx=j
dq.append((sy,sx,0,0))
visited[f].add((sy,sx))
while dq:
    cy, cx, f, step = dq.popleft()
    nf = f ^ 1 if mx[cy][cx] == '?' else f
    for dy,dx in dyx:
        ny,nx = cy + dy, cx + dx
        if 0<=ny<h and 0<=nx<w and mx[ny][nx] not in {door[nf], '#'} and (ny,nx) not in visited[nf]:
            if ny==gy and nx==gx:
                print(step+1)
                exit()
            visited[nf].add((ny,nx))
            dq.append((ny,nx,nf,step+1))
print(-1)            
            
        
    