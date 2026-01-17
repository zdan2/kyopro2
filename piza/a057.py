n=int(input())
mx=[[int(i) for i in input()] for _ in range(n)]
dyx=[(1,0),(0,1),(1,1),(1,-1)]
s=set()

def f(y, x, direc, pn):
    dy,dx=dyx[direc]
    cy,cx=y,x
    c=1
    nxt=mx[y][x]+pn

    while True:
        cy += dy
        cx += dx
        if not (0 <= cy < n and 0 <= cx < n):
            break
        if mx[cy][cx] != nxt:
            break

        s.add((cy, cx, direc))
        c += 1
        nxt += pn

    return c
    
r=0
for y in range(n):
    for x in range(n):
        for i,(dy,dx) in enumerate(dyx):
            ny=y+dy
            nx=x+dx
            if 0<=ny<n and 0<=nx<n:
                if abs(mx[y][x]-mx[ny][nx])==1:
                    if (y,x,i) not in s:
                        pn=mx[ny][nx]-mx[y][x]
                        r=max(r,f(y,x,i,pn)) 
print(r)