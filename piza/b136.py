n,h,w=map(int,input().split())
d={'F':(-1,0),'B':(1,0),'L':(0,-1),'R':(0,1)}
sy,sx=map(int,input().split())
sy-=1
sx-=1
di=list(input())
mx=[list(map(int,input().split())) for _ in range(h)]
for e in di:
    dy,dx=d[e]
    sy+=dy
    sx+=dx
    print(mx[sy][sx])