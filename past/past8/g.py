import heapq

n,k=map(int,input().split())

hq=[]

for _ in range(n):
    a,b,c=map(int,input().split())
    h=0
    for i in range(a):
        if len(hq)<k:
            heapq.heappush(hq,-(b+c*i))
        else:
            d=heapq.heappop(hq)
            if d>-(b+c*i):
                heapq.heappush(hq,d)
                h=1
            else:
                heapq.heappush(hq,-(b+c*i))
        if h:
            break
print(heapq.heappop(hq)*-1)

        

            
            