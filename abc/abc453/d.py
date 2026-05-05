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
q.append(([],sy,sx,-1))
visited.add((sy,sx,-1))
while q:
    rt,y,x,drec=q.popleft()
    if (y,x)==(gy,gx):
        print('Yes')
        print(''.join(['R' if e==0 else 'D' if e==1 else 'U' if e==2 else 'L' for e in rt]))
        exit()
    for i,(dy,dx) in enumerate(dyx):
        ny=y+dy
        nx=x+dx
        if 0<=ny<h and 0<=nx<w and (ny,nx,i) not in visited and mx[ny][nx]!='#':
            if (y,x) in os and drec==i:
                q.append((rt+[i],ny,nx,i))
                visited.add((ny,nx,i))
            elif (y,x) in xs and drec!=i:
                q.append((rt+[i],ny,nx,i))
                visited.add((ny,nx,i))
            elif (y,x) not in xs and (y,x) not in os:
                q.append((rt+[i],ny,nx,i))
                visited.add((ny,nx,i))
print('No')