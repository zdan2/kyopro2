n,m=map(int,input().split())
a=list(map(int,input().split()))
a=[e%m for e in a]
if len(set(a))==m:
    print(0)
    exit()
r=sum(a)
a.sort()
a.append(0)
a+=a
c=a[0]
b=float('inf')
for i in range(n*2):
    if a[i+1]==a[i] or a[i+1]==(a[i]+1)%m:
        c+=a[i+1]
    else:
        b=min(b,r-c)
        c=a[i+1]
b=min(b,r-c)
print(b)