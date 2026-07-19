from collections import Counter
from sortedcontainers import SortedList
t=int(input())
for _ in range(t):
    s=input()
    l=len(s)
    c=Counter(s).most_common()
    if c[0][1]>(l+1)//2:
        print('No')
        continue
    sc=SortedList(c,key=lambda x: -x[1])   
    t=[]
    while sc:
        lc,rc=0,0
        if sc:
            ll,lc=sc.pop(0)
            t.append(ll)
            lc-=1
        if sc:
            rl,rc=sc.pop(-1)
            t.append(rl)
            rc-=1
        if lc>0:
            sc.add((ll,lc))
        if rc>0:
            sc.add((rl,rc))
    print('Yes')
    print(''.join(t))
        