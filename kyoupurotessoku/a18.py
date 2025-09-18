n,s=map(int,input().split())
cards=list(map(int,input().split()))

dp=[False]*(s+1)
dp[0]=True

for card in cards:
    for i in range(s,-1,-1):
        if dp[i]==True and i+card<=s:
            dp[i+card]=True

if dp[-1]:
    print('Yes')
else:
    print('No')