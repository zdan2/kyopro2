from collections import defaultdict,deque
h,w=map(int,input().split())
mx=[list(input()) for _ in range(h)]
dyx=[(1,0),(0,1),(-1,0),(0,-1)]
warp=defaultdict(list)
for i in range(h):
    for j in range(w):
        if 'a'<=mx[i][j]<='z':
            warp[mx[i][j]].append((i,j))
dq=deque()
dq.append((0,0,0))
v=set()
va=set()
while dq:
    y,x,c=dq.popleft()
    if y==h-1 and x==w-1:
        print(c)
        exit()
    if 'a'<=mx[y][x]<='z' and mx[y][x] not in va:
        va.add(mx[y][x])
        for ny,nx in warp[mx[y][x]]:
            if (ny,nx) not in v:
                v.add((ny,nx))
                dq.append((ny,nx,c+1))
    for dy,dx in dyx:
        ny=y+dy
        nx=x+dx
        if 0<=ny<h and 0<=nx<w and (ny,nx) not in v and mx[ny][nx]!='#':
            v.add((ny,nx))
            dq.append((ny,nx,c+1))
print(-1)