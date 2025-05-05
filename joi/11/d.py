n,k=map(int,input().split())
menu={}
for _ in range(k):
    a,b=map(int,input().split())
    menu[a]=b
dp=[[0]*(n+1) for _ in range(3)]
for i in range(3):
    dp[i][1]=[1,0]
print(dp)