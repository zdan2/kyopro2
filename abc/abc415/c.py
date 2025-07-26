t=int(input())
for _ in range(t):
    n=int(input())
    s=list(input())
    dp=[False]*(2**n)
    dp[0]=True
    for e in range(1,2**n):
        if s[e-1]=='1':
            dp[e]=False
            continue
        for i in range(e.bit_length()):
            if e&(1<<i):
                m=e^(1<<i)
                if dp[m]:
                    dp[e]=True
                    break
    print('Yes' if dp[-1] else 'No')