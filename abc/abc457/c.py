n,k=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)]
for i,c in enumerate(map(int,input().split())):
    l=a[i][0]
    if l*c>=k:
        j=k%l
        if j==0:
            j=-1
        print(a[i][j])
        exit()
    k-=l*c