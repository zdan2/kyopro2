from collections import defaultdict
import heapq

n, m, q = map(int, input().split())

d = defaultdict(list)

for _ in range(m):
    a, b, c = map(int, input().split())
    d[a].append((b, c))
    d[b].append((a, c))

x = list(map(int, input().split()))

hq = []
heapq.heappush(hq, (0, 1)) 
for i,j in d[1]:
    heapq.heappush(hq,(j,i))

v = set()
r=[float('inf')]*(n+1)

for xi in x:
    can=[]
    while hq:
        nw, nxt = heapq.heappop(hq)
        if nw <= xi:
            v.add(nxt)
            r[nxt]=nw
            for k, n in d[nxt]:
                if r[k]>n:
                    can.append((n,k))
                    r[k]=n
        else:
            can.append((nw,nxt))
            break
    print(len(v))
    for e in can:
        heapq.heappush(hq,e)
