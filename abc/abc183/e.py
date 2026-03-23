from collections import deque,defaultdict
h,w=map(int,input().split())
mx=[list(input()) for _ in range(h)]
start=(0,0)
goal=(0,0)
d=defaultdict(list)
for i in range(h):
    for j in range(w):
        if mx[i][j]=='S':
            start=(i,j)
        elif mx[i][j]=='G':
            goal=(i,j)
        elif mx[i][j]!='.' and mx[i][j]!='#':
            d[mx[i][j]].append((i,j))
q=deque()
v=set()
u=set()
q.append((start,0))
v.add(start)
dyx=[(0,1),(1,0),(-1,0),(0,-1)]
while q:
    (y,x),c=q.popleft()
    if (y,x)==goal:
        print(c)
        exit()
    for dy,dx in dyx:
        ny=y+dy
        nx=x+dx
        if 0<=ny<h and 0<=nx<w and mx[ny][nx]!='#' and (ny,nx) not in v:
            q.append(((ny,nx),c+1))
            v.add((ny,nx))
    if mx[y][x]in d and mx[y][x] not in u:
                u.add(mx[y][x])
                for p in d[mx[y][x]]:
                    q.append((p,c+1))
                    v.add(p)
print(-1)