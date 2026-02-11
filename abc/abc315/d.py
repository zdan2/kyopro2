from sortedcontainers import SortedSet
h,w=map(int,input().split())
c=[list(input()) for _ in range(h)]
o=[[i,c[i]] for i in range(h)]
t=[]
row=SortedSet([i for i in range(h)])
col=SortedSet([i for i in range(w)])
for i,r in enumerate(zip(*c)):
    t.append([i,list(r)])
while True:
    cr=[]
    for idx,r in o:
        if len(r)>1 and len(set(r))==1:
            cr.append(idx)
    cc=[]        
    for idx,r in t:
        if len(r)>1 and len(set(r))==1:
            cc.append(idx)
    for i in cr[::-1]:
        idx=row.index(i)
        o.pop(idx)
    for i in cc[::-1]:
        idx=col.index(i)
        t.pop(idx)
    for i in cr[::-1]:
        idx=row.index(i)
        row.remove(i)
        for _,r in t:
            r.pop(idx)
    for i in cc[::-1]:
        idx=col.index(i)
        col.remove(i)
        for _,r in o:
            r.pop(idx)
    if not cr and not cc:
        break
res=0
for _,r in o:
    res+=len(r)
print(res)