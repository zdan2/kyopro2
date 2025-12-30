import heapq
n,k=map(int,input().split())
s=list(input())
hq=[]
for i,e in enumerate(s):
    heapq.heappush(hq,(e,i))
r=''
while hq and k>0:
    k-=1
    e,i=heapq.heappop(hq)
    r+=e
    
print(r+''.join(s))