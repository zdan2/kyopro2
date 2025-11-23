from collections import deque
dyx=[(1,0),(0,1),(-1,0),(0,-1)]
n=int(input())
mx=[list(input()) for _ in range(n)]
c=[[0]*n for _ in range(n)]
q=deque()
r=0
for i in range(n):
    for j in range(n):
        if mx[i][j]=='.':
            d=0
            for dy,dx in dyx:
                ny=i+dy
                nx=j+dx
                if 0<=ny<n and 0<=nx<n and mx[ny][nx]=='#':
                    d+=1
            if d>=3:
                q.append((i,j))
            c[i][j]=d
while q:
    y,x=q.popleft()
    mx[y][x]='#'
    r+=1
    for dy,dx in dyx:
        ny=y+dy
        nx=x+dx
        if 0<=ny<n and 0<=nx<n and mx[ny][nx]=='.':
            c[ny][nx]+=1
            if c[ny][nx]==3:
                q.append((ny,nx))
                mx[ny][nx]='!'
print(r)