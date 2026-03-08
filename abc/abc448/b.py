n,m=map(int,input().split())
c=list(map(int,input().split()))
r=0
for _ in range(n):
    a,b=list(map(int,input().split()))
    a-=1
    r+=min(b,c[a])
    c[a]=max(0,c[a]-b)
print(r)