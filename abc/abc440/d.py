from sortedcontainers import SortedSet

n,q=map(int,input().split())
a=SortedSet(list(map(int,input().split())))

for _ in range(q):
    l,d=map(int,input().split())
    r=l+d-1
    c=0
    
    while True:
        lidx=a.bisect_left(l)
        ridx=a.bisect_left(r)
        if lidx==ridx:
            break
        print('a',l,r,lidx,ridx,d)
        d-=a[ridx]-l-(ridx-lidx)-1
        print('d',d)
        l=r
        r=l+d
    print(r)