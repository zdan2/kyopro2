def dfs(mx,cp,y,x):
    s=[(y,x)]
    v=set()
    dyx=[(1,0),(0,1),(-1,0),(0,-1)]
    c=-1
    while s:
        cy,cx=s.pop()
        if (cy,cx) not in v:
            v.add((cy,cx))
            c+=1
            for dy,dx in dyx:
                ny=cy+dy
                nx=cx+dx
                if 0<=ny<n and 0<=nx<m and mx[ny][nx]=='.':
                    s.append((ny,nx))
    if c==cp:
        return True
    else:
        return False
                    
n,m=map(int,input().split())
mx=[list(input()) for _ in range(n)]

cp=0
for i in range(n):
    for j in range(m):
        if mx[i][j]=='.':
            cp+=1

r=0
for y in range(n):
    for x in range(m):
        if mx[y][x]=='#':
            h=dfs(mx,cp,y,x)
            if h:
                r+=1

print(r)

