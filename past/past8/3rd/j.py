n,q=map(int,input().split())
c=0
for _ in range(q):
    t,k=map(int,input().split())
    if t==1:
        if k>n:
            k=k-n
            if c&(1<<(k-1)):
                print(n-k+1)
            else:
                print(n+k)
        else:
            k=n-k
            if c&(1<<k):
                print(n+k+1)
            else:
                print(n-k)
    else:
        c^=2**k-1