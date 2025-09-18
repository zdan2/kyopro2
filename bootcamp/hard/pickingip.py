from bisect import bisect
n=int(input())
xy=[tuple(map(int,input().split())) for _ in range(n)]
if len(xy)==1:
    print(1)
    exit()
xy=sorted(xy)
x=[x for x,_ in xy]
y=[y for _,y in xy]
i=0
can=[0,1]
c=0
while x:
    x1=x[i]
    x2=x[bisect(x,x1)]
    y1=y[i]
    y2=y[bisect(x,x1)]
    dx=x2-x1
    dy=y2-y1
    for i in range(2,len(x)):
        #print(dx,dy,x1,y1,x[i],y[i])
        if (x[i]-x1)%dx==0:
            if (y[i]-y1)%dy==0 and (x[i]-x1)//dx==(y[i]-y1)//dy:
                can.append(i)
    print(can)
    for i in can[::-1]:
        x.pop(i)
        y.pop(i)
    c+=1
    if len(x)==1:
        c+=1
        break
    can=[0,1]
    i=0
print(c)
    
