from collections import deque
h,w,r,c,t=map(int,input().split())
mx=[list(input()) for _ in range(h)]
dyx=[(1,0),(-1,0),(0,1),(0,-1)]
q=deque()
q.append((r-1,c-1,0))
mx[r-1][c-1]=0
while q:
    y,x,now=q.popleft()
    if now>=t:
        continue
    for dy,dx in dyx:
        ny=y+dy
        nx=x+dx
        if 0<=ny<h and 0<=nx<w and mx[ny][nx]=='#':
            mx[ny][nx]=now+1
            q.append((ny,nx,now+1))
for i in range(h):
    for j in range(w):
       if isinstance(mx[i][j], int):
            if mx[i][j]<t:
                mx[i][j]='A'
            elif mx[i][j]==t:
                mx[i][j]='B'
for r in mx:
    print(''.join(r))