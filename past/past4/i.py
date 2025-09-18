n = int(input())
a = list(map(int, input().split()))
sum_a = sum(a)
aw = a + a
l = 0
sum_c = 0
can = float('inf')

for r in range(2 * n):
    sum_c += aw[r]
    while r - l + 1 > n:
        sum_c -= aw[l]
        l += 1
    while sum_c * 2 > sum_a and l <= r:
        can = min(can, abs(sum_a - 2 * sum_c))
        sum_c -= aw[l]
        l += 1
    can = min(can, abs(sum_a - 2 * sum_c))
    if can == 0:
        break

print(can)
