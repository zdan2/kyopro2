from collections import deque
h,w=map(int,input().split())
mx=[list(input()) for _ in range(h)]
dist=[[float('inf')]*w for _ in range(h)]
q=deque()
dyx=[(0,1,'<'),(0,-1,'>'),(1,0,'^'),(-1,0,'v')]
for i in range(h):
    for j in range(w):
        if mx[i][j]=='E':
            q.append((i,j,0))
while q:
    y,x,cur=q.popleft()
    for dy,dx,cd in dyx:
        ny=y+dy
        nx=x+dx
        if 0<=ny<h and 0<=nx<w and mx[ny][nx]!='#' and mx[ny][nx]!='E':
            if dist[ny][nx]>cur+1:
                dist[ny][nx]=cur+1
                q.append((ny,nx,cur+1))
                mx[ny][nx]=cd
for r in mx:
    print(''.join(r))