from collections import deque
h,w=map(int,input().split())
mx=[list(input()) for _ in range(h)]
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
        if mx[i][j]=='o':
            os.add((i,j))
        if mx[i][j]=='x':
            xs.add((i,j))
visited=set()
q=deque()
q.append((sy,sx,-1))
visited.add((sy,sx,-1))
wh=[[set() for _ in range(w)] for _ in range(h)]
print(wh)
while q:
    y,x,drec=q.popleft()
    if (y,x)==(gy,gx):
        print('Yes')
        for r in wh:
            print(r)
        exit()
    for i,(dy,dx) in enumerate(dyx):
        ny=y+dy
        nx=x+dx
        if 0<=ny<h and 0<=nx<w and (ny,nx,i) not in visited and mx[ny][nx]!='#':
            if (y,x) in os and drec==i:
                q.append((ny,nx,i))
                visited.add((ny,nx,i))
                wh[ny][nx].add(i)
            elif (y,x) in xs and drec!=i:
                q.append((ny,nx,i))
                visited.add((ny,nx,i))
                wh[ny][nx].add(i)
            elif (y,x) not in xs and (y,x) not in os:
                q.append((ny,nx,i))
                visited.add((ny,nx,i))
                wh[ny][nx].add(i)
print('No')
route=[]
v=set()
def dfs(y,x):
    if (y,x)==(sy,sx):
        return
    for nxt in wh[y][x]:
        route.append(nxt)
        ny=dyx[nxt][0]*-1
        nx=dyx[nxt][1]*-1
        v.add((y+ny,x+nx))
        dfs(ny,nx)
        route.pop()
        v.remove((y+ny,x+nx))
print(route)
        
    