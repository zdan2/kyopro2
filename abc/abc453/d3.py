from collections import deque

h,w=map(int,input().split())
mx=[list(input().strip()) for _ in range(h)]
dyx=[(0,1),(1,0),(-1,0),(0,-1)]

os=set()
xs=set()
sy,sx,gy,gx=0,0,0,0

for i in range(h):
    for j in range(w):
        if mx[i][j]=='S':
            sy,sx=i,j
        if mx[i][j]=='G':
            gy,gx=i,j

visited=set()
q=deque()
q.append((sy,sx,-1))
visited.add((sy,sx,-1))

wh=[[[None]*4 for _ in range(w)] for _ in range(h)]

goal=None

while q:
    y,x,drec=q.popleft()

    if (y,x)==(gy,gx):
        goal=(y,x,drec)
        break

    for i,(dy,dx) in enumerate(dyx):
        ny=y+dy
        nx=x+dx
        c=mx[y][x]
        if not (0<=ny<h and 0<=nx<w):
            continue
        if mx[ny][nx]=='#':
            continue
        if (ny,nx,i) in visited:
            continue
        if c=='o':
            if drec!=i:
                continue
        elif c=='x':
            if drec==i:
                continue

        visited.add((ny,nx,i))
        q.append((ny,nx,i))
        wh[ny][nx][i]=drec

if goal is None:
    print('No')
else:
    route=[]
    y,x,d=goal

    while (y,x,d)!=(sy,sx,-1):
        route.append(d)
        py=y-dyx[d][0]
        px=x-dyx[d][1]
        pd=wh[y][x][d]
        y,x,d=py,px,pd

    route.reverse()

    print('Yes')
    print(''.join('R' if e==0 else 'D' if e==1 else 'U' if e==2 else 'L' for e in route))