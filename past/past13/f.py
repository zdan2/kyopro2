import math
n=int(input())
a,b,c,d=map(int,input().split())
a*=1000
b*=1000
c*=1000
d*=1000
x=input().replace('.','')
x=int(x)
print(x)
s=a+2*b+3*c+4*d
l=0
r=10**13
while l<r:
    mid=(l+r+1)//2
    f=(s-x*mid*1000)/(x-1)
    print(f,mid)
    if f>x:
        l=mid+1
    else:
        r=mid-1
print(mid)