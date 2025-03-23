s=input()
h=len(s)
t=input()
w=len(t)
dp=[[0]*(w+1) for _ in range(h+1)]
for i in range(1,h+1):
    for j in range(1,w+1):
        if s[i-1]==t[j-1]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i][j-1],dp[i-1][j])
r = []
i, j = h, w
while i > 0 and j > 0:
    if s[i-1] == t[j-1]:
        r.append(s[i-1])
        i -= 1
        j -= 1
    else:
        if dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1
print(''.join(r[::-1]))