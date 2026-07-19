n, k = map(int, input().split())
a = list(map(int, input().split()))
ok = 0
ng = 10**20
while ng - ok > 1:
    mid = (ok + ng) // 2
    c = 0
    for i, e in enumerate(a):
        s = i + 1
        if mid > e:
            c += (mid - e + s - 1) // s
            if c > k:
                break
    if c <= k:
        ok = mid
    else:
        ng = mid
print(ok)