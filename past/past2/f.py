import heapq
n=int(input())
x=[]
for _ in range(n):
   a,b=map(int,input().split()) 
   heapq.heappush(x,(a,b))
y=[]
r=0
for i in range(1,n+1):
    while x:
        a,b=heapq.heappop(x)
        if a<=i:
            heapq.heappush(y,-b) 
        else:
            heapq.heappush(x,(a,b))
            break
    r-=heapq.heappop(y)
    print(r)    