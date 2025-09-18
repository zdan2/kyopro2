from collections import deque
h,w=map(int,input().split())
mx=[list(input()) for _ in range(h)]
rx=[[float('inf')]*w for _ in range(h)]
q=deque()
q.append((0,0))
rx[0][0]=0
while q:
    x,y=q.popleft()
    now_m=mx[x][y]
    now_c=rx[x][y]
    if x==h-1 and y==w-1:
        print(rx[x][y])
        exit()
    for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
        nx=x+dx
        ny=y+dy
        if 0<=nx<h and 0<=ny<w:
            if now_m!=mx[nx][ny]:
                if now_c+1<rx[nx][ny]:
                    rx[nx][ny]=now_c+1
                    q.append((nx,ny))
print(-1)