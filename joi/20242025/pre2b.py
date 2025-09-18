n,c=map(int,input().split())
a=list(map(int,input().split()))
p=list(map(int,input().split()))
if -1 not in p:
    print(-1)
    exit()
s=set(list(range(n)))
r=[]
while s:
    can=[]
    mc=max(s)
    v=set()
    while True:
        can.append(mc)
        s.discard(mc)
        mc=p[mc]
        if mc==-1:
            break
        else:
            mc-=1
            if mc not in v:
                v.add(mc)
            else:
                can=[]
                break

    r.append(can)
mm=0
for e in r:
    m=c
    now=-2
    for cp in e[::-1]:
        if m>=a[cp]:
            now=cp
            m-=a[cp]
            mm=max(mm,now)
        else:
            break
print(mm+1)
    