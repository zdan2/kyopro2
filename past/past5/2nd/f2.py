from collections import defaultdict,deque
dyx=[(0,-1),(-1,0),(0,1),(1,0)]
direc={'<':(0,-1),'^':(-1,0),'>':(0,1),'v':(1,0)}
h,w=map(int,input().split())
r,c=map(int,input().split())
mx=[list(input()) for _ in range(h)]
d=defaultdict(set)
for i in range(h):
    for j in range(w):
        if mx[i][j]!='#':
            if mx[i][j]=='>':
                if j+1<w and mx[i][j+1]!='#':
                    d[(i,j)].add((i,j+1))
            if mx[i][j]=='<':
                if j-1>=0 and mx[i][j-1]!='#':
                    d[(i,j)].add((i,j-1))
            if mx[i][j]=='^':
                if i-1>=0 and mx[i-1][j]!='#':
                    d[(i,j)].add((i-1,j))
            if mx[i][j]=='v':
                if i+1<h and mx[i+1][j]!='#':
                    d[(i,j)].add((i+1,j))
            if mx[i][j]=='.':
                for dy,dx in dyx:
                    ny=i+dy
                    nx=j+dx
                    if 0<=ny<h and 0<=nx<w and mx[ny][nx]!='#':
                        d[(ny,nx)].add((i,j))
                        d[(i,j)].add((ny,nx))
print(d)
q=deque()
q.append((r-1,c-1))
visited=set()
while q:
    now=q.popleft()
    if now not in visited:
        visited.add(now)
        for nxt in d[now]:
            if nxt not in visited:
                q.append(nxt)
for y,x in visited:
    mx[y][x]='o'
for r in mx:
    print(r)
        
    
