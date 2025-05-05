from collections import defaultdict
d=defaultdict(lambda:[None]*n)
n=int(input())
for i in range(n):
    m=int(input())
    for j in range(m):
        a,b=map(int,input().split())
        d[i][a-1]=b
ans=0
for i in range(2**n):
    h=1
    for j in range(n):
        xj=(i>>j)&1
        for k,e in enumerate(d[j]):
            if e==None:
                continue
            bk=(i>>k)&1
            if xj:
                if bk!=e:
                    h=0
                    break
        if h==0:
            break
    else:
        ans=max(ans,i.bit_count())
print(ans)