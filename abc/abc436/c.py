n,m=map(int,input().split())
s=set()
d=[(1,0),(0,1),(1,1)]
c=0
for _ in range(m):
    y,x=map(int,input().split())
    can=[(y,x)]
    for dy,dx in d:
        can.append((y+dy,x+dx))
    for e in can:
        if e in s:
            break
    else:
        for e in can:
            s.add(e)
        c+=1
print(c)