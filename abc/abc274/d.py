n,x,y=map(int,input().split())
a=list(map(int,input().split()))
ax=[]
ay=[]
for i in range(1,n):
    if i%2==1:
        ay.append(a[i])
    else:
        ax.append(a[i])
sx=set()
sx.add(a[0])
for e in ax:
    ns=set()
    for now in sx:
        ns.add(now+e)
        ns.add(now-e)
    sx=ns
sy=set()
sy.add(0)
for e in ay:
    ns=set()
    for now in sy:
        ns.add(now+e)
        ns.add(now-e)
    sy=ns
if x in sx and y in sy:
    print('Yes')
else:
    print('No') 