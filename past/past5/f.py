n,m=map(int,input().split())
drug=[]
for _ in range(m):
    a,b,c=map(int,input().split())
    drug.append(set([a,b,c]))
mc=float('inf')
for i in range(2**n):
    used=set()
    for j in range(n):
        if i&(1<<j):
            used.add(j+1)
    for d in drug:
        if d&used==d:
            break
    else:
        print('u',used)
        for e in range(n):
            if e not in used:
                used.add(e+1)
                for d in drug:
                    print('c',used,d,used&d)
                    if used&d!=d:
                        break
                else:
                    mc=min(mc,len(used)-1)
                    print(used)
                used.discard(e)
print(mc)