from collections import deque
h,w,d=map(int,input().split())
mx=[list(input()) for _ in range(h)]
kx=[['.']*w for _ in range(h)]
dyx=[(1,0),(0,1),(-1,0),(0,-1)]

for i in range(h):
    for j in range(w):
        if 

for i in range(h):
    for j in range(w):
        if mx[i][j]=='H':
            kx[i][j]='*'
            q=deque([(i,j,0)])
            while q:
                y,x,n=q.popleft()
                if n>=d:
                    break
                for dy,dx in dyx:
                    ny=y+dy
                    nx=x+dx
                    if 0<=ny<h and 0<=nx<w and kx[ny][nx]=='.':
                        kx[ny][nx]='*'
                        q.append((ny,nx,n+1))
                    elif abs(i-ny)+abs(j-nx)<=d:
                        q.append((ny,nx,n+1))
c=0
for i in range(h):
    for j in range(w):
        if kx[i][j]=='*' and mx[i][j]!='#':
            c+=1

print(c)