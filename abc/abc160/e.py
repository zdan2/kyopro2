import heapq
x,y,a,b,c=map(int,input().split())
p=list(map(int,input().split()))
p=[e*-1 for e in p]+[0]*(x+y)
q=list(map(int,input().split()))
q=[e*-1 for e in q]+[0]*(x+y)
r=list(map(int,input().split()))
r=[e*-1 for e in r]+[0]*(x+y)
heapq.heapify(p)
heapq.heapify(q)
heapq.heapify(r)
c=0
cx=1
cy=1
red=heapq.heappop(p)
blue=heapq.heappop(q)
white=heapq.heappop(r)
for _ in range(x+y):
    can=min(red,blue,white)
    c-=can
    if can==red:
        if cx<x:
            red=heapq.heappop(p)
            cx+=1
        else:
            red=0
    elif can==blue:
        if cy<y:
            blue=heapq.heappop(q)
            cy+=1
        else:
            blue=0
    else:
        white=heapq.heappop(r)  
print(c)
