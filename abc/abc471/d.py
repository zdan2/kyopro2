from sortedcontainers import SortedList
q, v = map(int, input().split())
hq = SortedList()
for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        now, w = query[1], query[2]
        hq.add(w - now)
    elif query[0] == 2:
        now = query[1]
        if not hq:
            print(-1)
            continue
        base = hq.pop(-1)
        print(min(base + now, v))