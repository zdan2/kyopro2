from collections import deque

h, w = map(int, input().split())
mx = [list(input()) for _ in range(h)]

dyx = [(1,0),(0,1),(-1,0),(0,-1)]
door = ['x', 'o']  # f=0 のとき 'o' が閉、f=1 のとき 'x' が閉（あなたの意図通り）

sy = sx = gy = gx = 0
for i in range(h):
    for j in range(w):
        if mx[i][j] == 'S':
            sy, sx = i, j
        if mx[i][j] == 'G':
            gy, gx = i, j

# visited[f] に (y,x)
visited = [set(), set()]
q = deque()

start_f = 0
visited[start_f].add((sy, sx))
q.append((sy, sx, start_f, 0))  # y, x, f, step

while q:
    cy, cx, f, step = q.popleft()

    # このマスが ? なら「次の遷移だけ」状態が変わる
    nf = f ^ 1 if mx[cy][cx] == '?' else f

    for dy, dx in dyx:
        ny, nx = cy + dy, cx + dx
        if not (0 <= ny < h and 0 <= nx < w):
            continue
        if mx[ny][nx] == '#':
            continue
        if mx[ny][nx] == door[nf]:   # 次状態 nf で閉じているドアは通れない
            continue
        if (ny, nx) in visited[nf]:
            continue

        if ny == gy and nx == gx:
            print(step + 1)
            exit()

        visited[nf].add((ny, nx))
        q.append((ny, nx, nf, step + 1))

print(-1)