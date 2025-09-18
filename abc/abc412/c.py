from bisect import bisect_left
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    sa=sorted(a[1:-1])
    r=a[-1]
    l=a[0]
    if n==2 and l*2>=r:
        print(2)
        continue
    elif n==2 and l*2<r:
        print(-1)
        continue
    if l*2>=r:
        print(2)
        continue
    c=2
    e=n-2
    while True:
        i=bisect_left(sa,(r+1)//2)
        if i==e:
            c=-1
            break
        c+=1
        r=sa[i]
        e=i
        if r<=2*l:
            break
        if e==0:
            c=-1
            break
    print(c)