n, k = map(int, input().split())
s = [tuple(map(int, input().split())) for _ in range(n)]

def count_leq(x):
    cnt = 0
    for a, b, c in s:
        if x < b:
            continue
        t = (x - b) // c + 1
        if t > a:
            t = a
        cnt += t
    return cnt
l = -10**18
r = 10**18
while l + 1 < r:
    mid = (l + r) // 2
    if count_leq(mid) >= k:
        r = mid
    else:
        l = mid

print(r)
