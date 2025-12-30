import heapq
h,w,z=map(int,input().split())
y,x=map(int,input().split())
y-=1
x-=1
mx=[list(map(int,input().split())) for _ in range(h)]
v=set()
v.add((y,x))
hq=[]
cur=mx[y][x]
dyx=[(1,0),(0,1),(-1,0),(0,-1)]
for dy,dx in dyx:
    if 0<=y+dy<h and 0<=x+dx<w:
        v.add((y+dy,x+dx))
        heapq.heappush(hq,(mx[y+dy][x+dx],y+dy,x+dx))
while hq and hq[0][0]<(cur+z-1)//z:
    hp,y,x=heapq.heappop(hq)
    cur+=hp
    for dy,dx in dyx:
        ny=y+dy
        nx=x+dx
        if 0<=ny<h and 0<=nx<w and (ny,nx) not in v:
            v.add((ny,nx))
            heapq.heappush(hq,(mx[ny][nx],ny,nx))
print(cur)