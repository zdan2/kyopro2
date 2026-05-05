from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))

mod = 10**9 + 7

pos = defaultdict(int)
neg = defaultdict(int)

pos[a[0] % mod] = 1

for e in a[1:]:
    np = defaultdict(int)
    nn = defaultdict(int)

    for f, v in pos.items():
        np[(f + e) % mod] = (np[(f + e) % mod] + v) % mod
        nn[(f - e) % mod] = (nn[(f - e) % mod] + v) % mod

    for f, v in neg.items():
        np[(f + e) % mod] = (np[(f + e) % mod] + v) % mod

    pos = np
    neg = nn

sum_p = sum(k * v % mod for k, v in pos.items()) % mod
sum_n = sum(k * v % mod for k, v in neg.items()) % mod

print((sum_p + sum_n) % mod)