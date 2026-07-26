from collections import deque
h,w=map(int,input().split())

mx=[['.']*(w+2)]+[['.']+list(input())+['.'] for _ in range(h)]+[['.']*(w+2)]
dyx=[(1,0),(0,1),(-1,0),(0,-1)]
r=[]
h+=2
w+=2
for i in range(h):
    for j in range(w):
        if mx[i][j]=='#':
            v=set()
            q=deque()
            q.append((i,j))
            area=0
            shore=0
            while q:
                y,x=q.popleft()
                area+=1
                v.add((y,x))
                for dy,dx in dyx:
                    ny=y+dy
                    nx=x+dx
                    if (ny,nx) in v:
                        continue
                    if 0<=ny<h and 0<=nx<w:
                        if mx[ny][nx]=='#':
                            v.add((ny,nx))
                            q.append((ny,nx))
                        else:
                            shore+=1
            r.append((area,shore))
            for a,b in v:
                mx[a][b]='.'
r=sorted(r,key=lambda x:[-x[0],-x[1]])
for e in r:
    print(*e)