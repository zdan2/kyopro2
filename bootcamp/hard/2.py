import heapq
from collections import defaultdict
n, x = map(int, input().split())
d = defaultdict(list)
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    d[a].append((c, b))
    d[b].append((c, a))
for i in range(1, n + 1):
    dist = [float('inf')] * (n + 1)
    dist[i] = 0
    hq = [(0, i)]
    while hq:
        cost, cur = heapq.heappop(hq)
        if cost > dist[cur]:
            continue
        if cost > x:
            break
        if cost == x:
            print("Yes")
            exit()
        for w, ne in d[cur]:
            new_cost = cost + w
            if new_cost < dist[ne] and new_cost <= x:
                dist[ne] = new_cost
                heapq.heappush(hq, (new_cost, ne))
print("No")