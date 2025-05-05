h,w=map(int,input().split())
mx=[list(input()) for _ in range(h)]
cmx=[r.copy() for r in mx]
t=[['.']*w for _ in range(h)]
dyx=[(0,1),(1,0),(0,-1),(-1,0),(1,-1),(-1,1),(1,1),(-1,-1)]
for i in range(h):
    for j in range(w):
        if mx[i][j]=='#':
            can=[]
            for dy,dx in dyx:
                y=i+dy
                x=j+dx
                if 0<=y<h and 0<=x<w:
                    if mx[y][x]!='#':
                        break
                    else:
                        can.append((y,x))
            else:
                t[i][j]='#'
                cmx[i][j]='.'
                for y,x in can:
                    cmx[y][x]='.'
for r in cmx:
    if '#' in r:
        print('impossible')
        exit()
print('possible')
for r in t:
    print(''.join(r))