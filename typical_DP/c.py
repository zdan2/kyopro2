n=int(input())
a=[list(map(int,input().split())) for _ in range(n-1)]
dp=[float('inf')]*(2**n)
dp[0]=0
for i in range(1,2**n):
    c=float('inf')
    for j in range(i.bit_length()):
        