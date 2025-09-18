n,m=map(int,input().split())
r=[]
for i in range(m):
    k=int(input())
    rr=[list(map(int,input().split())) for _ in range(k)]
    r.append(rr)
for i in range(2**n):
    h=True
    for rr in r:
        for idx,b in rr:
            idx-=1
            if (i>>idx)&1==b:
                break
        else:
            h=False
    if h:
        print('Yes')
        exit()
print('No')