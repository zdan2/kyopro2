n,x,y=map(int,input().split())
a=sorted(list(map(int,input().split())))
l=0
r=a[0]*y
h=-1
while l<=r:
    mid=(l+r)//2
    cy=mid//y
    cx=a[0]-cy
    target=cx*x+cy*y
    print(l,r,mid,target)
    for i in range(1,n):
        cx=(target-x*a[i])//(y-x)
        cy=a[i]-cx
        print(a[i],cx,cy)
        if cx*x+cy*y<target:
            r=mid-1
            break
        if cx*x+cy*y>target:
            l=mid+1
            break
    else:
        h=max(h,target)
print(h)