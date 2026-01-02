h,w,n=map(int,input().split())
b=[tuple(map(int,input().split())) for _ in range(n)]
bset=set(b)
dyx=[(1,0),(0,1),(-1,0),(0,-1),(1,-1),(-1,1),(1,1),(-1,-1)]
a=[0]*10
seen=set()
for y,x in b:
    for dy,dx in dyx+[(0,0)]:
        ny=y+dy
        nx=x+dx
        if 2<=ny<=h-1 and 2<=nx<=w-1 and (ny,nx) not in seen:
            seen.add((ny,nx))
            c=1 if (ny,nx) in bset else 0
            for ry,rx in dyx:
                if (ny+ry,nx+rx) in bset:
                    c+=1
            a[c]+=1
a[0]=(h-2)*(w-2)-len(seen)
for e in a:
    print(e)