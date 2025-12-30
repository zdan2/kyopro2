n,m=map(int,input().split())
bs=[0]*(n+1)
for _ in range(m):
    l,r=map(int,input().split())
    if l>r:
        l,r=r,l
    bs[l-1]+=1
    bs[r]-=1
for i in range(1,n+1):
    bs[i]+=bs[i-1]
print(*bs[:n])