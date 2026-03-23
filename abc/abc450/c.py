from collections import deque, defaultdict
h,w=map(int,input().split())
g=[list(input()) for _ in range(h)]
dyx=[(0,1),(1,0),(-1,0),(0,-1)]
v=set()
c=0
for i in range(h):
    for j in range(w):
        if (i,j) in v:
            continue
        if g[i][j]=='.':
            v.add((i,j))
            q=deque()
            q.append((i,j))
            l=False if i==0 or j==0 or i==h-1 or j==w-1 else True
            while q:
                y,x=q.popleft()
                for dy,dx in dyx:
                    ny=y+dy
                    nx=x+dx
                    if 0<=ny<h and 0<=nx<w and g[ny][nx]=='.' and (ny,nx) not in v:
                        if ny==0 or nx==0 or ny==h-1 or nx==w-1:
                            l=False
                        q.append((ny,nx))
                        v.add((ny,nx))
            if l:
                c+=1
print(c)    