from collections import deque
h,w=map(int,input().split())
s=[list(input()) for _ in range(h)]
mx=[['.']*w for _ in range(h)]
dyx=[(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)]
q=deque()
t=[[float('inf')]*w for _ in range(h)]
for i in range(h):
    for j in range(w):
        if s[i][j]=='#':
            mx[i][j]='.'
            for dy,dx in dyx:
                ny=i+dy
                nx=j+dx
                if 0<=ny<h and 0<=nx<w and s[ny][nx]=='.' and mx[ny][nx]=='.':
                    mx[ny][nx]='#'
                    t[ny][nx]=1
                    q.append((ny,nx,1))
while q:
    y,x,c=q.popleft()
    for dy,dx in dyx:
        ny=y+dy
        nx=x+dx
        if 0<=ny<h and 0<=nx<w and mx[ny][nx]=='.' and t[ny][nx]>c+1:
            t[ny][nx]=c+1
            q.append((ny,nx,c+1))
for r in t:
    print(''.join(['#' if e%2==0 else '.' for e in r]))