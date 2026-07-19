n=int(input())
a=list(map(int,input().split()))
sa=sum(a)
dp=[[[float('inf')]*sa for _ in range(sa)] for _ in range(n)]
dp[0][sa][0]=0
for i in range(n):
    for j in range(sa):
        for k in 