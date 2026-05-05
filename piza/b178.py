from collections import deque

n, m = map(int, input().split())
mx = [[-1 for _ in range(m)] for _ in range(n)]
k = int(input())
dyx = [(1, 0), (0, 1), (-1, 0), (0, -1)]

q = deque()
for _ in range(k):
    y, x, t = map(int, input().split())
    y -= 1
    x -= 1
    mx[y][x] = t
    q.append((y, x))

tmp = int(input())

while q:
    step_size = len(q)
    targets = set()
    
    for _ in range(step_size):
        cy, cx = q.popleft()
        for dy, dx in dyx:
            ny, nx = cy + dy, cx + dx
            if 0 <= ny < n and 0 <= nx < m and mx[ny][nx] == -1:
                targets.add((ny, nx))
    updates = []
    for ny, nx in targets:
        th = 0
        co = 0
        for dy, dx in dyx:
            nny, nnx = ny + dy, nx + dx
            if 0 <= nny < n and 0 <= nnx < m and mx[nny][nnx] >= 0:
                th += mx[nny][nnx]
                co += 1
        
        if co > 0:
            updates.append((ny, nx, th // co))
    for ny, nx, val in updates:
        mx[ny][nx] = val
        q.append((ny, nx))

ans = sum(1 for r in mx for e in r if e >= tmp)
print(ans)