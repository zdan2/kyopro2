n, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

need = (k * k) // 2 + 1

l = 0
r = 10**9 + 1

def ok(mid):
    mx = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(n):
        for j in range(n):
            val = 1 if a[i][j] >= mid else 0
            mx[i + 1][j + 1] = val + mx[i][j + 1] + mx[i + 1][j] - mx[i][j]

    mn = 10**18

    for i in range(n - k + 1):
        for j in range(n - k + 1):
            cnt = mx[i + k][j + k] - mx[i][j + k] - mx[i + k][j] + mx[i][j]
            mn = min(mn, cnt)

    return mn >= need


while r - l > 1:
    mid = (l + r) // 2

    if ok(mid):
        l = mid
    else:
        r = mid

print(l)