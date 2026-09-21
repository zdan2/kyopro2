n,k=map(int,input().split())
a=list(map(int,input().split()))

def can(mid):
    c=1
    cur=0
    for x in a:
        if cur+x>mid:
            c+=1
            cur=x
        else:
            cur+=x
    return c<=k

ng=max(a)-1
ok=sum(a)
while ok-ng>1:
    mid=(ok+ng)//2
    if can(mid):
        ok=mid
    else:
        ng=mid
print(ok)