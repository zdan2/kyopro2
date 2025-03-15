n,m,k,q=map(int,input().split())
a=[]
b=[]
for _ in range(n):
    p,t=map(int,input().split())
    if t==0:
        a.append(p)
    else:
        b.append(p)

a.sort(reverse=True)
b.sort(reverse=True)
print(a)
print(b)
dp=[[float('inf')]*(m+1) for _ in range(k)]
kc=k
dp[0][1]=a.pop()
dp[k-1][1]=b.pop()
for i in range(2,m):
    if a:
        ac=a.pop()
    else:
        ac=float('inf')
    if b:
        bc=b.pop()
    else:
        bc=float('inf')
        
    for j in range(k):
        dp[j][i]=min(dp[j][i-1]+a,dp[j]
            
    
    