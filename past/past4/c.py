n,m=map(int,input().split())
mx=[list(input()) for _ in range(n)]

dyx=[(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(-1,1),(1,-1),(0,0)]
cx=[[0]*m for _ in range(n)]
for y in range(n):
    for x in range(m):
        c=0
        for dy,dx in dyx:
            nx=x+dx
            ny=y+dy
            if 0<=ny<n and 0<=nx<m and mx[ny][nx]=='#':
                c+=1
        cx[y][x]=str(c)

for r in cx:
    print(''.join(r))
            
            