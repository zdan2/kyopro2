h,w=map(int,input().split())
mx=[list(input()) for _ in range(h)]
q=[]
c=0
dyx=[(1,0),(0,1),(-1,0),(0,-1)]
for i in range(h):
    for j in range(w):
        if mx[i][j]=='#':
            q.append((i,j,[(i,j)]))
            c+=1
if c==1:
    print(c)
    y,x,route=q.pop()
    print(y+1,x+1)
    exit()
while q:
    y,x,route=q.pop()
    for dy,dx in dyx:
        ny=y+dy
        nx=x+dx
        if 0<=ny<h and 0<=nx<w:
            if mx[ny][nx]=='#' and (ny,nx) not in route:
                nr=route+[(ny,nx)]
                q.append((ny,nx,nr))
                if len(nr)==c:
                    print(c)
                    for y,x in nr:
                        print(y+1,x+1)
                    exit() 