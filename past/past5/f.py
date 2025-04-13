n,m=map(int,input().split())
drug=[]
for _ in range(m):
    a,b,c=map(int,input().split())
    drug.append(set([a,b,c]))
c=0
r=[]
for i in range(2**n):
    used=set()
    for j in range(n):
        if i&(1<<j):
            used.add(j+1)
    for d in drug:
        for i in range(n):
            cused=used.copy()
            can=cused.add(i)
            if can&d==d:
                break
    else:
        r.append(used)
print(r)