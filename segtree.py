class SegTree:
    def __init__(self, a, mode="min"):
        self.n = len(a)
        self.op = min if mode == "min" else max
        inf = float("inf") if mode == "min" else -float("inf")
        self.e = (inf, inf)

        self.tree = [self.e] * self.n + [
            (x, i) for i, x in enumerate(a)
        ]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.op(self.tree[i * 2],
                                  self.tree[i * 2 + 1])

    # i番目の値をxに変更
    def update(self, i, x):
        p = i + self.n
        self.tree[p] = (x, i)
        while p > 1:
            p //= 2
            self.tree[p] = self.op(self.tree[p * 2],
                                  self.tree[p * 2 + 1])

    # 区間[l, r)の(値, インデックス)を返す
    def query(self, l, r):
        l += self.n
        r += self.n
        ans = self.e
        while l < r:
            if l % 2:
                ans = self.op(ans, self.tree[l])
                l += 1
            if r % 2:
                r -= 1
                ans = self.op(ans, self.tree[r])
            l //= 2
            r //= 2
        return ans
    
n, m = map(int, input().split())
p = list(map(int, input().split()))

seg_min = SegTree(p, "min")
seg_max = SegTree(p, "max")

for _ in range(m):
    l, r = map(int, input().split())
    l -= 1

    min_v, min_idx = seg_min.query(l, r)
    max_v, max_idx = seg_max.query(l, r)

    for seg in (seg_min, seg_max):
        seg.update(min_idx, max_v)
        seg.update(max_idx, min_v)

    p[min_idx], p[max_idx] = max_v, min_v

print(*p)