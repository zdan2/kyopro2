from collections import deque
def bfs(mx,sy,sx,gy,gx):
    sy-=1
    sx-=1
    gy-=1
    gx-=1
    q=deque()
    q.append((sy,sx))
    v=set()
    mx[sy][sx]=0
    dyx=[(0,1),(1,0),(-1,0),(0,-1)]
    h=len(mx)
    w=len(mx[0])
    while q:
        y,x=q.popleft()
        if (y,x)==(gy,gx):
            return mx[y][x]
        if (y,x) not in v:
            v.add((y,x))
            c=mx[y][x]
            for dy,dx in dyx:
                ny=y+dy
                nx=x+dx
                if 0<=ny<h and 0<=nx<w and mx[ny][nx]=='.':
                    mx[ny][nx]=c+1
                    q.append((ny,nx))
            



h,w=map(int,input().split())
sy,sx=map(int,input().split())
gy,gx=map(int,input().split())
mx=[list(input()) for _ in range(h)]

print(bfs(mx,sy,sx,gy,gx))
