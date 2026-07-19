import heapq
a,b,c,d=map(int,input().split())
hq=[1]
heapq.heapify(hq)
e=1
s=set()
for i in range(d):
    e=heapq.heappop(hq)
    if e*a not in s:
        s.add(e*a)
        heapq.heappush(hq,e*a)
    if e*b not in s:
        s.add(e*b)
        heapq.heappush(hq,e*b)
    if e*c not in s:
        s.add(e*c)
        heapq.heappush(hq,e*c)
print(e)