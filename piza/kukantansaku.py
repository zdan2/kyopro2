n,x,k=map(int,input().split())
a=list(map(int,input().split()))

mc=0
c=0
for i in range(n):
    if a[i]<x:
        c+=1
    else:
        mc=max(mc,c)
        c=0
mc=max(mc,c)
print(mc)
