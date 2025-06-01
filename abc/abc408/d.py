t = int(input())
for _ in range(t):
    n=int(input())
    s=list(input())
    co=s.count('1')
    cur=0
    best=0
    for e in s:
        if e=='1':
            x=1
        else:
            x=-1
        cur=max(x,cur+x)
        best=max(best,cur)
    print(co-best)