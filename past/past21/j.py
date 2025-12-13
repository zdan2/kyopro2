from collections import deque
n=int(input())
mx=[list(input()) for _ in range(n)]
d={(-1,0):(0,-1),(0,-1):(1,0),(1,0):(0,1),(0,1):(-1,0)}
v=set()
vwo=set()
q=deque([((1,1),(-1,0)),((1,1),(0,-1))])
while q:
    print(v)
    print(vwo)
    pos,direc=q.popleft()
    y,x=pos
    dy,dx=direc
    py=y-dy
    px=x-dx
    ny,nx=d[direc]
    cy=py+ny
    cx=px+nx
    if mx[py][px]=='.':
        v.add((py,px))
        if ((py,px),direc) not in vwo:
            q.append(((py,px),direc))
            vwo.add((((py,px),direc)))
    else:
        nxt_y,nxt_x=d[direc]
        if mx[y-nxt_y][x-nxt_x]=='.':
            if ((py,px),d[direc]) not in vwo:
                q.append(((py,px),d[direc]))
                vwo.add(((py,px),d[direc]))
    if mx[cy][cx]=='#':
        if ((py,px),d[direc]) not in vwo:
            q.append(((py,px),d[direc]))
            vwo.add(((py,px),d[direc]))
print(len(v))