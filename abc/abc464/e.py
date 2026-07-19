h,w,q=map(int,input().split())
mx=[[0]*w for _ in range(h)]
d={0:'A'}
for i in range(1,q+1):
    r,c,x=input().split()
    r=int(r)-1
    c=int(c)-1
    d[i]=x
    mx[r][c]=i
for i in range(h-2,-1,-1):
    for j in range(w):
        if mx[i+1][j]>mx[i][j]:
            mx[i][j]=mx[i+1][j]
for j in range(w-2,-1,-1):
    for i in range(h):
        if mx[i][j+1]>mx[i][j]:
            mx[i][j]=mx[i][j+1]
for i in range(h):
    for j in range(w):
        mx[i][j]=d[mx[i][j]]
for l in mx:
    print(''.join(l))