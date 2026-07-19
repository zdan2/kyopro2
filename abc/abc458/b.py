h,w=map(int,input().split())
m=[]
for i in range(h):
    r = [4 - (i in (0, h - 1)) - (j in (0, w - 1)) for j in range(w)]
    m.append(r)
if h==1:
    m[0]=[e-1 for e in m[0]]
if w==1:
    for r in m:
        r[0]-=1
for r in m:
    print(*r)