n=int(input())
mx=[list(map(int,input().split())) for _ in range(n)]
zi,zj=0,0
for i in range(n):
    for j in range(n):
        if mx[i][j]==0:
            zi,zj=i,j
            break
c=0
for a in range(1,n+1):
    mx[zi][zj]=a
    for k in range(n):
        if mx[a-1][k]!=mx[zi][mx[zj][k]-1]:
            break
    else:
        print(a)
        c+=1
print(c)