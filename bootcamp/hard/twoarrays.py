n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
sa=sum(a)
sb=sum(b)
x=sb-sa
if x<0:
    print('No')
    exit()
ca=0
cb=0
for i in range(n):
    if a[i]<b[i]:
        ca+=(b[i]-a[i]+1)//2
    else:
        cb+=a[i]-b[i]
if x>=ca and x>=cb:
    print('Yes')
else:
    print('No')