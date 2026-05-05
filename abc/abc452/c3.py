from collections import defaultdict

n = int(input())
q = [tuple(map(int, input().split())) for _ in range(n)]
m = int(input())

a = [input().strip() for _ in range(m)]
mx = defaultdict(set)

for s in a:
    l = len(s)
    for i, ch in enumerate(s, 1):
        mx[(l, i)].add(ch)

for w in a:
    if len(w) != n:
        print('No')
        continue

    ok = True
    for i, ch in enumerate(w):
        y, x = q[i]
        if ch not in mx[(y, x)]:
            ok = False
            break

    print('Yes' if ok else 'No')