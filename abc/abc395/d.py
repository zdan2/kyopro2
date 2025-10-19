from bisect import bisect
n,q=map(int,input().split())
pi=[(i,0) for i in range(n+1)]
nest=[[[0],[i]] for i in range(n+1)]
for i in range(q):
    a=list(map(int,input().split()))
    if a[0]==1:
        pi[a[1]]=(a[2],i)
    if a[0]==2:
        nest[a[1]][0].append(i)
        nest[a[1]][1].append(a[2])
        nest[a[2]][0].append(i)
        nest[a[2]][1].append(a[1])
    if a[0]==3:
        cur_nest,now=pi[a[1]]
        root=[]
        while True:
            idx=bisect(nest[cur_nest][0],now)
            if idx>=len(nest[cur_nest][0]):
                break
            root.append((cur_nest,idx))
            now=nest[cur_nest][0][idx]
            cur_nest=nest[cur_nest][1][idx]
        final_nest=cur_nest
        for nest_update,idx_update in root:
            nest[nest_update][1][idx_update]=final_nest

        pi[a[1]]=(final_nest,now)
        print(final_nest)