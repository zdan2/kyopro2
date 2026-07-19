from collections import deque
h,w=map(int,input().split())
m=[list(input()) for _ in range(h)]
t=[[[False]*4 for _ in range(w)] for _ in range(h)]
start=(0,0,0)
goal=(0,0)
for i in range(h):
    for j in range(w):
        if m[i][j]=='S':
            start=(i,j,4)
        if m[i][j]=='G':
            goal=(i,j)
q=deque()
q.append(start)
dyx=[(1,0),(0,1),(-1,0),(0,-1)]
while q:
    y,x,fr=q.popleft()
    if (y,x)==goal:
        break
    if fr<4:
        dy,dx=dyx[fr]
        ny=y+dy
        nx=x+dx
        if 0<=ny<h and 0<=nx<w and m[ny][nx]!='#':
            if not t[ny][nx][fr]:
                t[ny][nx][fr]=True
                if m[ny][nx]=='o':
                    q.append((ny,nx,fr))
                else:
                    q.append((ny,nx,4))
    else:
        for i,(dy,dx) in enumerate(dyx):
            ny=y+dy
            nx=x+dx
            if 0<=ny<h and 0<=nx<w and m[ny][nx]!='#':
                if not t[ny][nx][i]:
                    t[ny][nx][i]=True
                    if m[ny][nx]=='o':
                        q.append((ny,nx,i))
                    else:
                        q.append((ny,nx,4))
for r in t:
    print(r)