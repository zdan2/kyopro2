n,k=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
f=list(map(int,input().split()))
f.sort(reverse=True)
for i in range(n):
    cur=a[i]
    a[i]=max(a[i]-k,0)
    k-=cur
    if k<=0:
        break
print(a)
print(f)
print(max(x*y for x,y in zip(a,f)))    