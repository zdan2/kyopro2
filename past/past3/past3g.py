from collections import deque

n, x, y = map(int, input().split())
x += 201
y += 201

mx = [[float('inf')] * 403 for _ in range(403)]
directions = [(1, 1), (0, 1), (-1, 1), (1, 0), (-1, 0), (0, -1)]

# 障害物の設定
for _ in range(n):
    i, j = map(int, input().split())
    i += 201
    j += 201
    if 0 <= j < 403 and 0 <= i < 403:
        mx[j][i] = -1  # 障害物は -1 に設定

# BFS の初期化
q = deque([(201, 201, 0)])

# BFS の実行
while q:
    yy, xx, dist = q.popleft()
    if mx[yy][xx] == -1:
        continue  # 障害物の場合はスキップ
    if mx[yy][xx] <= dist:
        continue  # 既により短い距離で訪問済みの場合はスキップ
    mx[yy][xx] = dist
    for dx, dy in directions:
        nx = xx + dx
        ny = yy + dy
        if 0 <= ny < 403 and 0 <= nx < 403:
            if mx[ny][nx] != -1 and mx[ny][nx] > dist + 1:
                q.append((ny, nx, dist + 1))

# 結果の出力
if 0 <= y < 403 and 0 <= x < 403:
    result = mx[y][x]
    if result == float('inf'):
        print(-1)
    else:
        print(int(result))
else:
    print(-1)
