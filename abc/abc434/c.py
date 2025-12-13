q=int(input())
for _ in range(q):
    n,h=map(int,input().split())
    v=0
    high=h
    low=h
    p=True
    for i in range(n):
        t,l,u=map(int,input().split())
        high+=t-v
        low=max(0,low-(t-v))
        if l<=low<=high<=u or low<=l<=high or low<=u<=high:
            high=min(u,high)
            low=max(low,l)
            v=t
        else:
            p=False
    print('Yes' if p else 'No')