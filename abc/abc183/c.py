x1,y1=map(int,input().split())
x2,y2=map(int,input().split())
if x1==x2 and y1==y2:
    print(0)
elif x1+y1==x2+y2 or x1-y1==x2-y2 or abs(x1-x2)+abs(y1-y2)<=3:
    print(1)
elif (x1+y1)%2==(x2+y2)%2 or abs(x1-x2)+abs(y1-y2)<=6:
    print(2)
else:
    dx=x1-x2
    dy=y1-y2
    for nx,ny in [(x2,y1+dx),(x1+dy,y2),(x2,y1-dx),(x1-dy,y2)]:
        if abs(nx-x2)+abs(ny-y2)<=3:
            print(2)
            break
    else:
        print(3)