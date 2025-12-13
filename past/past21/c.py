n,k=map(int,input().split())
for _ in range(n):
    s,t=map(int,input().split())
    a=(s+k-1)//k
    print(min(k*a,t)-s,end=' ')