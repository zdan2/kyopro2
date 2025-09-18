n,y,x=map(int,input().split())
s=list(input())
dd={'N':(1,0),'S':(-1,0),'W':(0,1),'E':(0,-1)}
fire=(0,0)
obs=(y,x)
smoke=set()
smoke.add(fire)
t=''
for wd in s:
    fy,fx=fire
    dy,dx=dd[wd]
    fire=(fy+dy,fx+dx)
    smoke.add(fire)
    oy,ox=obs
    obs=(oy+dy,ox+dx)
    if obs in smoke:
        t+='1'
    else:
        t+='0'
print(t)