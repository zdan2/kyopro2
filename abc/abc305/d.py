from bisect import bisect_right
n=int(input())
a=list(map(int,input().split()))
sl=[0]+[a[i] for i in range(1,n,2)]
slp=[(a[i],a[i+1]) for i in range(1,n,2)]
t=[0,slp[0][1]-slp[0][0]]
for e in slp[1:]:
    t.append(t[-1]+e[1]-e[0])
slp=[(0,0)]+slp
m=int(input())
for _ in range(m):
    l,r=map(int,input().split())
    lidx=bisect_right(sl,l)-1
    ridx=bisect_right(sl,r)-1
    a=t[ridx]-t[lidx]
    if slp[lidx][1]>l:
        a+=slp[lidx][1]-l
    if slp[ridx][1]>r:
        a-=slp[ridx][1]-r
    print(a)