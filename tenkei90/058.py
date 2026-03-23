n,k=map(int,input().split())

l=k.bit_length()
dp=[[i for i in range(100000)] for _ in range(l)]
for i in range(1,l):
    for j in range(10000):
        m=dp[i-1][j]
        c=m
        while m>0:
            c+=m%10
            m//=10
        dp[i][j]=dp[i-1][dp[i-1][c%100000]]
r=[]
for i in range(l+1):
    if n&(1<<i):
        r.append(i)
nxt=n
for z in r[::-1]:
    nxt=dp[]
