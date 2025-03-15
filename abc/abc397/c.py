n=int(input())
a=list(map(int,input().split()))
l=[0]*(n+1)
s=set()
for i in range(n):
    s.add(a[i])
    l[i+1]=len(s)
r=[0]*(n+1)
s=set()
for i in range(n-1,-1,-1):
    s.add(a[i])
    r[i]=len(s)

mc=0
for i in range(n+1):
    mc=max(l[i]+r[i],mc)
print(mc)
