dyx={0:[(0,-1),(0,1)],1:[(-1,0),(1,0)],2:[(0,1),(0,-1)],3:[(1,0),(-1,0)]}
h,w,sy,sx,n=map(int,input().split())
mx=[list(input()) for _ in range(h)]
d=0
y=sy
x=sx
f=0
mx[sy][sx]='*'
for _ in range(n):
    qx=input().split()
    q=qx[0]
    m=int(qx[1])
    if q=='L':
        idx=0
        r=-1
    else:
        idx=1
        r=1
    dy,dx=dyx[d][idx]
    for _ in range(m):
        y+=dy
        x+=dx
        if 0<=y<h and 0<=x<w and mx[y][x]!='#':
            mx[y][x]='*'
            continue
        else:
            f=1
            break
    if f:
        break
    d=(d+r)%4         
for r in mx:
    print(''.join(r)) 