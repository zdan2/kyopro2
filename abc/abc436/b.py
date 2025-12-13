n=int(input())
x=[[0]*n for _ in range(n)]
r=0
c=(n-1)//2
k=1
for _ in range(n*n):
    x[r][c]=k
    nr=(r-1)%n
    nc=(c+1)%n
    if x[nr][nc]!=0:
        r=(r+1)%n
    else:
        r=nr
        c=nc
    k+=1
for l in x:
    print(*l)