from collections import deque

h,w,k=map(int,input().split())
mx=[list(input()) for _ in range(h)]

def bfs(mx,s):
    r=0
    y,x=s
    if mx[y][x]=='#':
        return r
    dyx=[(1,0),(0,1),(-1,0),(0,-1)]
    q=deque([(y,x,0)])
    v=set()
    
    while q:
        y,x,c=q.popleft()
        if c==k:
            r+=1
        if (y,x) not in v:
            v.add((y,x))
            for dy,dx in dyx:
                ny=y+dy
                nx=x+dx
                if 0<=ny<h and 0<=nx<w and mx[ny][nx]=='.' and (ny,nx) not in v:
                    q.append((ny,nx,c+1))
    return r
c=0
for i in range(h):
    for j in range(w):
        r=bfs(mx,(i,j))
        print(i,j,r)
        c+=r

print(c)