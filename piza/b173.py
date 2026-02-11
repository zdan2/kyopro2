def comb2(n: int) -> int:
    return n * (n + 1) // 2

def comb3(n: int) -> int:
    return n * (n + 1) * (n + 2) // 6

N = int(input())
pairs = []
chars = set()
m=list(map(int,input().split()))
s=list(input().split())
for e in s:
    h, t = e[0], e[-1]
    pairs.append((h, t))
    chars.add(h)
    chars.add(t)
chars = sorted(chars)
idx = {ch: i for i, ch in enumerate(chars)}
M = len(chars)

cnt = [[0] * M for _ in range(M)]
for h, t in pairs:
    cnt[idx[h]][idx[t]] += 1
ans = 0
for x in range(M):
    ans += comb3(cnt[x][x])
for a in range(M):
        row_a = cnt[a]
        for b in range(M):
            n_ab = row_a[b]
            if n_ab == 0:
                continue
            row_b = cnt[b]
            for c in range(M):
                n_ac = row_a[c]
                if n_ac == 0:
                    continue
                n_bc = row_b[c]
                if n_bc == 0:
                    continue
                if b == c:
                    if a == b:
                        continue
                    ans += comb2(n_ab) * n_bc
                else:
                    ans += n_ab * n_ac * n_bc
print(ans)