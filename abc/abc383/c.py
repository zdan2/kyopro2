from collections import deque

h,w,d=map(int,input().split())
mx=[list(input()) for _ in range(h)]

dyx=[(1,0),(0,1),(-1,0),(0,-1)]

q=deque()
v=[[False]*w for _ in range(h)]

for i in range(h):
    for j in range(w):
        if mx[i][j]=='H':
            mx[i][j]='*'
            q.append((i,j,0))
            v[i][j]=True
            
while q:
    y,x,n=q.popleft()
    if n==d:
        continue
    for dy,dx in dyx:
        ny=y+dy
        nx=x+dx
        if 0<=ny<h and 0<=nx<w:
            if (mx[ny][nx]=='.' or mx[ny][nx]=='*') and not v[ny][nx]:
                v[ny][nx]=True
                mx[ny][nx]='*'
                q.append((ny,nx,n+1))
c=0
for r in mx:
    c+=r.count('*')
print(c)            