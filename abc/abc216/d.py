from collections import deque
n,m=map(int,input().split())
qs=[]
d={}
for i in range(n):
    k=int(input())
    a=deque(list(map(int,input().split())))
    c=a[0]
    qs.append(a)
    if c not in d:
        d[c]=i
        continue
    while c in d:
        qi=d[c]
        del d[c]
        qs[qi].popleft()
        a.popleft()
        if a:
            nxtc=a[0]
        else:
            nxtc=-1
        if qs[qi]:
            d[qs[qi][0]]=qi
        if nxtc>0 and nxtc not in d:
            d[nxtc]=i
            break
        c=nxtc
if not d:
    print('Yes')
else:
    print('No')