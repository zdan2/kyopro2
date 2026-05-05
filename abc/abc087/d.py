import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)


class WeightedDSU:
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]
        self.size = [1] * (n + 1)
        self.weight = [0] * (n + 1)

    def find(self, x):
        if self.parent[x] == x:
            return x
        p = self.parent[x]
        r = self.find(p)
        self.weight[x] += self.weight[p]
        self.parent[x] = r
        return r

    def potential(self, x):
        self.find(x)
        return self.weight[x]

    def diff(self, a, b):
        return self.potential(b) - self.potential(a)

    def merge(self, a, b, w):
        ra = self.find(a)
        rb = self.find(b)
        wa = self.weight[a]
        wb = self.weight[b]
        if ra == rb:
            return wb - wa == w
        if self.size[ra] < self.size[rb]:
            self.parent[ra] = rb
            self.weight[ra] = wb - wa - w
            self.size[rb] += self.size[ra]
        else:
            self.parent[rb] = ra
            self.weight[rb] = w + wa - wb
            self.size[ra] += self.size[rb]
        return True

n, m = map(int, input().split())
uf = WeightedDSU(n)
for _ in range(m):
    l, r, d = map(int, input().split())
    if not uf.merge(l, r, d):
        print("No")
        exit()
print("Yes")