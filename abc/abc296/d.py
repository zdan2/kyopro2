from math import isqrt

n, m = map(int, input().split())

# そもそも不可能
if n * n < m:
    print(-1)
    exit()

lo = max(1, (m + n - 1) // n)   # これ未満は b > n
hi = min(n, isqrt(m))
if hi * hi < m:
    hi += 1                     # ceil(sqrt(m))

best = None

for a in range(lo, hi + 1):
    b = (m + a - 1) // a
    if b < a:
        break

    p = a * b
    if best is None or p < best[2]:
        best = (a, b, p)

print(best[2])