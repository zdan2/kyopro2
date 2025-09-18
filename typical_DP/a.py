n=int(input())
a=list(map(int,input().split()))
sa=sum(a)
dp=[-1]*(sa+1)
dp[0]=0
for e in a:
    for i in range(sa,-1,-1):
        if dp[i]==0:
            dp[i+e]=0
print((sa+1)+sum(dp))    