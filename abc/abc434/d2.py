n = int(input())

rectangles = []
max_x = 0
max_y = 0

for _ in range(n):
    y1, y2, x1, x2 = map(int, input().split())
    rectangles.append((x1, y1, x2, y2))
    max_x = max(max_x, x2)
    max_y = max(max_y, y2)

imos = [[0] * (max_x + 1) for _ in range(max_y + 1)]

rem=2000*2000-max_x*max_y
for x1, y1, x2, y2 in rectangles:
    imos[y1][x1] += 1
    imos[y1][x2] -= 1
    imos[y2][x1] -= 1
    imos[y2][x2] += 1

for y in range(max_y + 1):
    for x in range(1, max_x + 1):
        imos[y][x] += imos[y][x - 1]

for y in range(1, max_y + 1):
    for x in range(max_x + 1):
        imos[y][x] += imos[y - 1][x]

ans = 0
for r in imos:
    print(r)
