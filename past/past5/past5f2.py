from itertools import product

n, m = map(int, input().split())
s = [tuple(map(int, input().split())) for _ in range(m)]
s = [ (a-1, b-1, c-1) for a, b, c in s ]

mc = 0
for pr in product([0, 1], repeat=n):
    found_all_ones = False
    c1, c2, c3 = 0, 0, 0
    for a, b, c in s:
        if pr[a] == 1 and pr[b] == 1 and pr[c] == 1:
            found_all_ones = True
            break 
    if found_all_ones:
        continue
    for a, b, c in s:
        if pr[a] == 1 and pr[b] == 1:
            c1 += 1
        if pr[a] == 1 and pr[c] == 1:
            c2 += 1
        if pr[b] == 1 and pr[c] == 1:
            c3 += 1
    mc = max(c1, c2, c3, mc)
print(mc)
