h,w,m=map(int,input().split())
mx=[[0]*w for _ in range(h)]
s=set(tuple(map(int,input().split())) for _ in range(m))
if (1,1) in s:
    mx[0][0]=1
for i in range(1,h):
    if (i+1,1) in s:
        mx[i][0]=mx[i-1][0]+1
    else:
        mx[i][0]=mx[i-1][0]
for j in range(1,w):
    if (1,j+1) in s:
        mx[0][j]=mx[0][j-1]+1
    else:
        mx[0][j]=mx[0][j-1]
for i in range(1,h):
    for j in range(1,w):
        mx[i][j]=max(mx[i-1][j],mx[i][j-1])
        if (i+1,j+1) in s:
            mx[i][j]+=1
print(mx[-1][-1])
        