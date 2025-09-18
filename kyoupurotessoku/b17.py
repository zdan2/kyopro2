n=int(input())
c=list(map(int,input().split()))
a=[abs(c[i-1]-c[i]) for i in range(1,n)]
b=[abs(c[i-2]-c[i]) for i in range(2,n)]

dp=[(float('inf'),-1) for _ in range(n)]
dp[0]=(0,-1)
dp[1]=(a[0],0)

for i in range(2,n):
    one = dp[i-1][0]+a[i-1]
    two = dp[i-2][0]+b[i-2]
    if one<=two:
        dp[i]=(one,i-1)
    else:
        dp[i]=(two,i-2)

root=[n]
now=n-1
while now!=-1:
    nxt=dp[now][1]
    root.append(nxt+1)
    now=nxt
print(len(root)-1)
print(*root[:-1][::-1])
        
    
