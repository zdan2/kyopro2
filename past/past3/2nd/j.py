from bisect import bisect
n,m=map(int,input().split())
child=[0]*n
a=list(map(int,input().split()))
a=a[::-1]
while a:
    sushi=a.pop()*-1
    idx=bisect(child,sushi)
    if idx==n:
        print(-1)
    else:
        print(idx+1)
        child[idx]=sushi