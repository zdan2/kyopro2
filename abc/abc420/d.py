from collections import deque
h,w=map(int,input().split())
mx=[list(input()) for _ in range(h)]
for i in range(h):
    for j in range(w):
        if mx[i][j]=='S':
            s=(i,j)
        if mx[i][j]=='G':
            g=(i,j)
dyx=[(1,0),(0,1),(-1,0),(0,-1)]
q=deque([(s[0],s[1],0,0)])
v0=set()
v1=set()
r=float('inf')
while q:
    y,x,c,p=q.popleft()
    if (y,x)==g:
        r=min(r,p)
    if c%2==1 and (y,x) in v0:
        continue
    if c%2==0 and (y,x) in v1:
        continue
    if c%2==0:v1.add((y,x))
    if c%2==1:v0.add((y,x))
    if c%2==0:
        f='o'
    else:
        f='x'    
    for dy,dx in dyx:
        ny,nx=y+dy,x+dx
        if 0<=ny<h and 0<=nx<w:
            if mx[ny][nx]=='.' or mx[ny][nx]==f or mx[ny][nx]=='G':
                q.append((ny,nx,c,p+1))
            if mx[ny][nx]=='?':
                q.append((ny,nx,c+1,p+1))
if r==float('inf'):
    print(-1)
else:
    print(r)