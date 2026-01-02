import heapq
n=int(input())
a=list(map(int,input().split()))
h2=[]
h3=[]
for e in a:
    if e%2==0:
        heapq.heappush(h2,e)
    else:
        heapq.heappush(h3,e)

while h2:
    e=heapq.heappop(h2)
    e//=2
    if e%2==1:
        heapq.heappush(h3,e)
    else:
        heapq.heappush(h2,e)
    if h2 and h3 and h2[0]<h3[0]:
        heapq.heapreplace(h2,h2[0]*3)
    elif h2 and not h3:
        heapq.heapreplace(h2,h2[0]*3)
    else:
        heapq.heapreplace(h3,h3[0]*3)
print(h3[0])       
        