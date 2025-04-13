import math
n=int(input())
a,b,c,d=map(int,input().split())
x=input().replace('.','')
x=int(x)
print(x)
s=a+2*b+3*c+4*d
l=0
r=10**13
mid=(l+r+1)//2
while l<r:
    f=(s-x*mid)//(mid-1)
    if f<x:
        l=mid+1
    else:
        r=mid-1
print(r)