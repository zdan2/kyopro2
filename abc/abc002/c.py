x1,y1,x2,y2,x3,y3=map(int,input().split())
(x1,y1),(x2,y2),(x3,y3)=sorted([(x1,y1),(x2,y2),(x3,y3)])
l=x1
r=x3
u=max(y1,y2,y3)
b=min(y1,y2,y3)
base=(r-l)*(u-b)
if y1<y2<y3:
    d1=(u-b)*abs(x1-x2)/2
    d2=(r-l)*abs(y2-y3)/2
    d3=(u-b)*(r-l)/2
elif y1>y2>y3:
    d1=(r-l)*abs(y1-y2)/2
    d2=(u-b)*abs(x2-x3)/2
    d3=(u-b)*(r-l)/2
else:
    d1=abs(x1-x2)*abs(y1-y2)/2
    d2=abs(x1-x3)*abs(y1-y3)/2
    d3=abs(x2-x3)*abs(y2-y3)/2
print(base-d1-d2-d3)