def pb(x1,y1,x2,y2):
    a=2*(x2-x1)
    b=2*(y2-y1)
    c=(x2*x2+y2*y2)-(x1*x1+y1*y1)
    return a,b,c
n=int(input())
for _ in range(n):
    x1,y1,x2,y2,x3,y3,x4,y4=map(int,input().split())
    a1,b1,c1=pb(x1,y1,x2,y2)
    a2,b2,c2=pb(x3,y3,x4,y4)
    if a1*b2-a2*b1==0:
        if a1*c2-a2*c1==0 and b1*c2-b2*c1==0:
            print('Yes')
        else:
            print('No')
    else:
        print('Yes') 