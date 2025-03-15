from collections import defaultdict
h,w=map(int,input().split())
mx=[list(input()) for _ in range(h)]
dyx=[(1,0),(0,1),(-1,0),(0,-1)]
g=defaultdict(set)
for i in range(h):
    for j in range(w):
        if mx[i][j]=='#':
            for dy,dx in dyx:
                y=i+dy
                x=j+dx
                if 0<=y<h and 0<=x<w and mx[y][x]=='#':
                    g[(i,j)].add((y,x))
sorted_dict=sorted(g.items(),key=lambda x:len(x[1]))
sy,sx=sorted_dict[0][0]
q=[(sy,sx)]
sorted_dict=dict(sorted_dict)
v=set()
route=[]
c=0
while q:
    now=q.pop()
    if now not in v:
        v.add(now)
        route.append(now)
        c+=1
        for nxt in sorted_dict[now]:
            if nxt not in v:
                q.append(nxt)
    elif q:
        nxt=q.pop()
        q.append(now)
        q.append(nxt)
                
for a,b in route:
    print(a+1,b+1)

