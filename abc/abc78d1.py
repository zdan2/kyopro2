h, w, k = map(int, input().split())
mx = [list(input()) for _ in range(h)]

def dfs(y, x, c, visited):
    if mx[y][x] == '#' or (y, x) in visited:
        return 0
    if c == k:
        return 1
    res = 0
    visited.add((y, x))
    for dy, dx in [(1,0), (0,1), (-1,0), (0,-1)]:
        ny = y + dy
        nx = x + dx
        if 0 <= ny < h and 0 <= nx < w:
            res += dfs(ny, nx, c + 1, visited)
    visited.remove((y, x))
    return res

total = 0
for i in range(h):
    for j in range(w):
        if mx[i][j] == '.':
            total += dfs(i, j, 0, set())

print(total)
