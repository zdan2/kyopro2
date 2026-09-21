h,w=map(int,input().split())
mx=[list(map(int,input().split())) for _ in range(h)]
d={mx[i][j]:(i,j) for j in range(w) for i in range(h)}
q=list(map(int,input().split()))
row=[0]*h
col=[0]*w
ans=0
for e in q:
    ans+=1
    y,x=d[e]
    row[y]+=1
    col[x]+=1
    if row[y]==w or col[x]==h:
        print(ans)
        break