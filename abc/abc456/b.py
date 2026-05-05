a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))
r=0
h={4,5,6}
for i in a:
    if i not in h:
        continue
    s=set()
    s.add(i)
    for j in b:
        if j not in h:
            continue
        d=s.copy()
        d.add(j)
        for k in c:
            if k not in h:
                continue
            e=d.copy()
            e.add(k)
            if e==h:
                r+=1 
print(r/216)