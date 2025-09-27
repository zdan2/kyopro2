t=int(input())
for _ in range(t):
    h,w=map(int,input().split())
    y=[i+1 for i in range(0,h-1,2)]
    x=[i+1 for i in range(0,w-1,2)]
    can=[]
    for i in y:
        for j in x:
            if i==h-1:
                i-=1
            if j==w-1:
                j-=1
            can.append((i,j))
    mx=[list(input()) for _ in range(h)]
    d=[[(-1,-1),(-1,0),(0,-1)],[(1,-1),(1,0),(0,-1)],[(-1,1),(-1,0),(0,1)],[(1,1),(0,1),(1,0)]]
    r=0
    print(can)
    for y,x in can:
        if mx[y][x]=='.':
            continue
        f=False
        for dyx in d:
            c=1
            for dy,dx in dyx:
                ny=y+dy
                nx=x+dx
                if mx[ny][nx]=='#':
                    c+=1
            if c==4:
                f=True
                print(y,x)
        if f:
            mx[y][x]='.'
            r+=1
    print(r)

