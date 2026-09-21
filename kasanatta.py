h,w,n=map(int,input().split())
mx=[[0]*(w+1) for _ in range(h+1)]
for _ in range(n):
    y1,x1,y2,x2=map(int,input().split())
    y1-=1
    x1-=1
    mx[y1][x1]+=1
    mx[y2][x1]-=1
    mx[y1][x2]-=1
    mx[y2][x2]+=1
for i in range(h):
    for j in range(w):
        mx[i][j+1]+=mx[i][j]
for j in range(w):
    for i in range(h):
        mx[i+1][j]+=mx[i][j]
b=max(max(r) for r in mx)
c=0
for i in range(h):
    for j in range(w):
        if mx[i][j]==b:
            c+=1
print(b,c)