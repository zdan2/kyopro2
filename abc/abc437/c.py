import heapq

n=int(input())
for _ in range(n):
    t=int(input())
    r=[tuple(map(int,input().split())) for _ in range(t)]
    r=sorted(r,key=lambda x:[-x[1],x[0]+x[1]])
    hq=[]
    s=set()
    for i,(a,b) in enumerate(r):
        heapq.heappush(hq,(a+b,a,b,i))
    i=0
    p=0
    while hq:
        if p<=0:
            while True:
                if i not in s:
                    s.add(i)
                    p+=r[i][1]
                    i+=1
                    break
                i+=1

        else:
            _,a,b,i=heapq.heappop(hq)
            if i not in s:
                
                
            
            