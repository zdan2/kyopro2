s=int(input())
mod=1000000007
w=s//3
dp=[[0]*(w+1) for _ in range(s+1)]
dp[0][0]=1
ss=0
for j in range(w):
    for i in range(ss,s+1):
        for k in range(s-i,2,-1):
            if i+k<=s:
                dp[i+k][j+1]+=dp[i][j]%mod
                dp[i+k][j+1]%=mod
    ss+=3
for r in dp:
    print(r)
            
            
