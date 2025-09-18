n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a.sort()
b.sort()
t=1
c=-1
if n==2:
    if a[0]>b[0]:
        print(-1)
        exit()
    if a[1]<=b[0]:
        print(a[0])
    else:
        print(a[1])
    exit()
for i in range(n-2,-1,-1):
    if a[i+t]>b[i] and t==1:
        c=a[i+1]
        t=0
    elif a[i]>b[i] and t==0:
        print(-1)
        exit()
if a[i]>b[i] and t==0:
    print(-1)
    exit()
if c==-1:
    print(a[0])
else:
    print(c)
        