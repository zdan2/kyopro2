from collections import deque

n = int(input())

tree = [[] for _ in range(n + 1)]
edges = []

for i in range(n - 1):
    a, b = map(int, input().split())
    edges.append((a, b))
    tree[a].append((b, i))
    tree[b].append((a, i))

max_color = max(len(tree[v]) for v in range(1, n + 1))
ans = [0] * (n - 1)
dq = deque([(1, 0, 0)])

while dq:
    now, parent, parent_color = dq.popleft()

    color = 1

    for nxt, edge_id in tree[now]:
        if nxt == parent:
            continue

        if color == parent_color:
            color += 1

        ans[edge_id] = color
        dq.append((nxt, now, color))

        color += 1

print(max_color)

for color in ans:
    print(color)