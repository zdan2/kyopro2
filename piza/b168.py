op=[(0,0,0),(0,0,1),(0,1,0),(1,0,0),(0,1,1),(1,0,1),(1,1,0),(1,1,1)]
a=list(input())
a=[int(e) for e in a]
b=list(input())
b=[int(e) for e in b]
c=list(input())
c=[int(e) for e in c]
d=[a,b,c]
can=[]
for e in d:
    s=set()
    for o in op:
        r=e[0]
        for i,p in enumerate(o):
            if p==0:
                r-=e[i+1]
            else:
                r+=e[i+1]
        s.add(r)
    can.append(s)
res=can[0]&can[1]&can[2]
if res:
    print('YES')
    print(*sorted(res))
else:
    print('NO')