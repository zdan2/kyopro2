n, q = map(int, input().split())
x = [tuple(map(int, input().split())) for _ in range(q)][::-1]

r = [1] * n
cur = [1] * n
pa = [i for i in range(n)]
u = set()

def find(v):
    while pa[v] != v:
        pa[v] = pa[pa[v]]
        v = pa[v]
    return v

for c, p in x:
    c -= 1
    p -= 1

    if c not in u:
        u.add(c)

        root_c = find(c)
        root_p = find(p)

        if root_c == root_p:
            continue

        r[root_p] += r[root_c]
        cur[root_p] += r[root_c]
        cur[root_c] -= r[root_c]

        pa[root_c] = root_p

print(*cur)