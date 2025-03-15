n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

dp=[(10**9,[]) for _ in range(n)]
dp[0]=(0,-1)
dp[1]=(a[0],0)

for i in range(2,n):
    if dp[i-1][0]+a[i-1]<=dp[i-2][0]+b[i-2]:
        dp[i]=(dp[i-1][0]+a[i-1],i-1)
    else:
        dp[i]=(dp[i-2][0]+b[i-2],i-2)

root=[n]
now=n-1
while now!=-1:
    nxt=dp[now][1]
    root.append(nxt+1)
    now=nxt
    
print(len(root)-1)
print(*root[:-1][::-1])
    
    