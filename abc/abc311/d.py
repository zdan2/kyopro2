from collections import deque
n,m=map(int,input().split())
vwd=set()
v=set()
v.add((1,1))
mx=[list(input()) for _ in range(n)]
dyx=[(1,0),(0,1),(-1,0),(0,-1)]
dq=deque([(1,1)])
while dq:
    y,x=dq.popleft()
    for i,(dy,dx) in enumerate(dyx):
        ny=y+dy
        nx=x+dx
        if 0<=ny<n and 0<=nx<m and mx[ny][nx]=='.' and (ny,nx,i) not in vwd:
            while True:
                vwd.add((ny,nx,i))
                v.add((ny,nx))
                ny+=dy
                nx+=dx
                if mx[ny][nx]=='#':
                    dq.append((ny-dy,nx-dx))
                    break
print(len(v))
        