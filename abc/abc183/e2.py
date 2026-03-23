from collections import deque, defaultdict

h, w = map(int, input().split())
mx = [list(input()) for _ in range(h)]
start = (0, 0)
goal = (0, 0)
d = defaultdict(list)

# 1. 辞書を作る際のバグ修正（'#' は登録しない）
for i in range(h):
    for j in range(w):
        if mx[i][j] == 'S':
            start = (i, j)
        elif mx[i][j] == 'G':
            goal = (i, j)
        elif mx[i][j] != '.' and mx[i][j] != '#':
            d[mx[i][j]].append((i, j))

q = deque()
q.append((start, 0))

v = set()
v.add(start) # キューに入れた瞬間に訪問済みにする！
u = set()

dyx = [(0, 1), (1, 0), (-1, 0), (0, -1)]
r = float('inf')

while q:
    (y, x), c = q.popleft()
    
    if (y, x) == goal:
        r = c
        break # BFSなので、最初に見つかったものが必ず最短

    # --- A. 上下左右への通常の移動 (コスト +1) ---
    for dy, dx in dyx:
        ny = y + dy
        nx = x + dx
        if 0 <= ny < h and 0 <= nx < w and mx[ny][nx] != '#' and (ny, nx) not in v:
            v.add((ny, nx)) # キューに追加する前に訪問済みにする
            q.append(((ny, nx), c + 1))
            
    # --- B. 今いるマスからのワープ移動 (コスト +1) ---
    current_char = mx[y][x]
    if current_char in d and current_char not in u:
        u.add(current_char) # この文字のワープは使用済みにする
        for ny, nx in d[current_char]:
            if (ny, nx) not in v:
                v.add((ny, nx)) # キューに追加する前に訪問済みにする
                q.append(((ny, nx), c + 1))

if r != float('inf'):
    print(r)
else:
    print(-1)