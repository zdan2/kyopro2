from collections import deque,defaultdict
n=int(input())
d=defaultdict(int)
x=0
hap=0
r=[]
for _ in range(n):
    w,h,b=map(int,input().split())
    if b>=h:
        x+=w
        hap+=b
    else:
        r.append([w,h,b])
q=deque([0,x,hap])


