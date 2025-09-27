from collections import deque
h,w=map(int,input().split())
mx=[list(input()) for _ in range(h)]
dyx=[(0,1),(1,0),(-1,0),(0,-1)]
s=deque()
r=0
for i in range(h):
    for j in range(w):
        if mx[i][j]=='#':
            r+=1
        if mx[i][j]=='.':
            c=0
            for dy,dx in dyx:
                ny=i+dy
                nx=j+dx
                if 0<=ny<h and 0<=nx<w and mx[ny][nx]=='#':
                    c+=1
                    if c==2:
                        break
            if c==1:
                s.append((i,j))

while s:
    l=len(s)
    for y,x in s:
        r+=1
        mx[y][x]='#'
    for _ in range(l):
        y,x=s.popleft()
        for dy,dx in dyx:
            ny=y+dy
            nx=x+dx
            if 0<=ny<h and 0<=nx<w and mx[ny][nx]=='.':
                c=0
                for dy,dx in dyx:
                    nny=ny+dy
                    nnx=nx+dx
                    if 0<=nny<h and 0<=nnx<w and mx[nny][nnx]=='#':
                        c+=1
                        if c==2:
                            break
                if c==1:
                    s.append((ny,nx))
print(r)