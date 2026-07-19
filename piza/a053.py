from collections import deque
h,w=map(int,input().split())
mx=[list(input()) for _ in range(h)]
RGB={'R':0,'G':0,'B':0}
dyx=[(1,0),(0,1),(-1,0),(0,-1)]
for i in range(h):
    for j in range(w):
        if mx[i][j] in RGB:
            color=mx[i][j]
            RGB[color]+=1
            q=deque()
            q.append([i,j])
            mx[i][j]='O'
            while q:
                y,x=q.popleft()
                for dy,dx in dyx:
                    ny=y+dy
                    nx=x+dx
                    if 0<=ny<h and 0<=nx<w and mx[ny][nx]==color:
                        q.append([ny,nx])
                        mx[ny][nx]='O'
print(RGB['R'],RGB['G'],RGB['B'])