n,q=map(int,input().split())
a=list(map(int,input().split()))
a=[x-1 for x in a]
dp=[[0]*n for _ in range(30)]
dp[0]=a
for k in range(1,30):
    for i in range(n):
        dp[k][i]=dp[k-1][dp[k-1][i]]
for _ in range(q):
    x,y=map(int,input().split())
    x-=1
    r=[]
    l=y.bit_length()
    for i in range(l):
        if y&(1<<i):
            r.append(i)
    nxt=x
    for z in r[::-1]:
        nxt=dp[z][nxt]
    print(nxt+1)