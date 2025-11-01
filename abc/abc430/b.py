n,m=map(int,input().split())
s=[list(input()) for _ in range(n)]
c=[]
for i in range(0,n-m+1):
    for j in range(0,n-m+1):
        z=[]
        for k in range(i,i+m):
            z.append(tuple(s[k][j:j+m]))
        c.append(tuple(z))
print(len(set(c)))