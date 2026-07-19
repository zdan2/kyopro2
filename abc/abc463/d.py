n,k=map(int,input().split())
s=[list(map(int,input().split())) for _ in range(n)]
s=sorted(s,key=lambda x:[x[1],x[0]])
def f(n):
    c=0
    l_r=-1
    for l,r in s:
        if l_r==-1:
            c+=1
            l_r=r
        elif l-l_r>=n:
            c+=1
            l_r=r
    return c>=k
ok=0
ng=10**10
while ng-ok>1:
    mid=(ng+ok)//2
    if f(mid):
        ok=mid
    else:
        ng=mid
if ok==0:
    print(-1)
else:
    print(ok)