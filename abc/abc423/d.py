import heapq
n,k=map(int,input().split())
hq=[]
c=0
now=0
for _ in range(n):
    a,b,d=map(int,input().split())
    now=max(now,a)
    if c+d<=k:
        c+=d
        print(now)
        heapq.heappush(hq,(a+b,d))
    else:
        while c+d>k:
            time,p=heapq.heappop(hq)
            c-=p
            if time>a:
                a=time
        now=max(a,now)
        print(now)
        heapq.heappush(hq,(time+b,d))