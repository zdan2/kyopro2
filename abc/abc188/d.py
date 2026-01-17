from collections import deque
n,w=map(int,input().split())
a=[]
for _ in range(n):
    x,y,c=map(int,input().split())
    a.append((x,c))
    a.append((y+1,-c))
a.sort()
now=0
cost=0
r=0
for day,v in a:
    if day!=now:
        r+=min(w,cost)*(day-now)
        now=day
    cost+=v
print(r)