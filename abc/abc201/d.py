h,w=map(int,input().split())
a=[list(input()) for _ in range(h)]
b=[[[0,0]]*w for _ in range(h)]
for i in range(1,w):
    j=i%2
    b[0][i]=b[0][i-1].copy()
    if a[0][i]=='-':
        b[0][i][j]=b[0][i-1][j]-1
    else:
        b[0][i][j]=b[0][i-1][j]+1
for i in range(1,h):
    j=i%2
    b[i][0]=b[i-1][0].copy()
    if a[i][0]=='-':
        b[i][0][j]=b[i-1][0][j]-1
    else:
        b[i][0][j]=b[i-1][0][j]+1
for i in range(1,h):
    for j in range(1,w):
        k=(i+j)%2
        up=b[i-1][j][k]-b[i-1][j][k^1]
        left=b[i][j-1][k]-b[i][j-1][k^1]
        if up<left:
            b[i][j]=b[i-1][j].copy()
        else:
            b[i][j]=b[i][j-1].copy()
        if a[i][j]=='-':
            b[i][j][k]-=1
        else:
            b[i][j][k]+=1
ao,ta=b[-1][-1]
print('Takahashi' if ta>ao else 'Aoki' if ao>ta else 'Draw')