def f(a,b):
    b=sorted(b)
    dp=[0]*(len(b)+1)
    for w,v in a:
        for i in range(len(b)):
            if w<=b[i] and v>dp[i+1]:
                dp[i+1]=v
                break
    return sum(dp)

n,m,q=map(int,input().split())
baggage=sorted([tuple(map(int,input().split())) for _ in range(n)],key=lambda x:-x[1])
box=list(map(int,input().split()))
for _ in range(q):
    l,r=map(int,input().split())
    can=box[:l-1]+box[r:]
    print(f(baggage,can))