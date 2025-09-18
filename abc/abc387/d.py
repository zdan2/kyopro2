from collections import deque
h,w=map(int,input().split())
s=[list(input()) for _ in range(h)]
for i in range(h):
    for j in range(w):
        if s[i][j]=='S':
            sy=i
            sx=j
        if s[i][j]=='G':
            gy=i
            gx=j
            s[i][j]='.'
mx=[[[float('inf'),float('inf')] for _ in range(w)] for _ in range(h)]
mx[sy][sx][0]=0
mx[sy][sx][1]=0
dyx=[[(0,1),(0,-1)],[(1,0),(-1,0)]]
q=deque()
q.append((sy,sx,0))
q.append((sy,sx,1))
while q:
    y,x,d=q.popleft()
    for dy,dx in dyx[d]:
        ny=y+dy
        nx=x+dx
        if 0<=ny<h and 0<=nx<w and s[ny][nx]=='.':
            if mx[ny][nx][d]>mx[y][x][(d+1)%2]+1:
                mx[ny][nx][d]=mx[y][x][(d+1)%2]+1
                q.append((ny,nx,(d+1)%2))
r=min(mx[gy][gx])
if r==float('inf'):
    print(-1)
else:
    print(r)