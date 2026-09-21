from collections import deque
h,w,k=map(int,input().split())
mx=[list(input()) for _ in range(h)]
bx=set()
by=set()
for i in range(h):
    for j in range(w):
        if mx[i][j]=='#':
            bx.add(j)
            by.add(i)
sx=set(range(w))^bx
sy=set(range(h))^by
p=deque()
v=set()
for y in sy:
    for x in sx:
        p.append((y,x,0))
        v.add((y,x))
dyx=[(1,0),(0,1),(-1,0),(0,-1)]
while p:
    cy,cx,step=p.popleft()
    if step==k:
        continue
    for dy,dx in dyx:
        ny=cy+dy
        nx=cx+dx
        if 0<=ny<h and 0<=nx<w and mx[ny][nx]=='.' and (ny,nx) not in v:
            v.add((ny,nx))
            p.append((ny,nx,step+1))
print(len(v))