from bisect import bisect
n,m,k=map(int,input().split())
x,y=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a.sort()
ca=[0]
for i in range(n):
    ca.append(ca[-1]+a[i])
dp=[[0]*2 for _ in range(m+1)]
dp[0][0]=bisect(ca,x+y*k)
dp[0][1]
for i in range(1,m):
    dp[i][0]=