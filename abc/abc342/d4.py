from math import isqrt
from collections import defaultdict

def er(n):
    if n < 2:
        return []
    f = [True] * (n + 1)
    f[0] = f[1] = False
    for i in range(2, isqrt(n) + 1):
        if f[i]:
            for j in range(i * i, n + 1, i):
                f[j] = False
    return [i for i, e in enumerate(f) if e]

n = int(input())
a = list(map(int, input().split()))

mx = max(a)
prime = er(isqrt(mx))

def kernel(x):
    if x == 0:
        return 0
    res = 1
    for p in prime:
        if p * p > x:
            break
        cnt = 0
        while x % p == 0:
            x //= p
            cnt ^= 1
        if cnt:
            res *= p
    if x > 1:
        res *= x
    return res

cnt = defaultdict(int)

z = a.count(0)
ans = z * (n - z) + z * (z - 1) // 2 

for x in a:
    if x == 0:
        continue
    k = kernel(x)
    ans += cnt[k]
    cnt[k] += 1

print(ans)