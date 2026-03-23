n,q=map(int,input().split())
d={i:set() for i in range(1,n+1)}
c=n
for _ in range(q):
    a=list(map(int,input().split()))
    t=a[0]
    if t==1:
        x=a[1]
        y=a[2]
        if not d[x]:
            c-=1
        if not d[y]:
            c-=1
        d[x].add(y)
        d[y].add(x)
    else:
        x=a[1]
        if d[x]:
            c+=1
        if d[x]:
            for p in d[x]:
                d[p].remove(x)
                if not d[p]:
                    c+=1
        d[x]=set() 
    print(c)