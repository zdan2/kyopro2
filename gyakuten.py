class BIT:
    def __init__(self, N):
        self.N = N
        self.bits = [0] * (self.N + 1)
    def update(self, i, x):
        while i <= self.N:
            self.bits[i] += x
            i += i & -i
    def total(self, i):
        res = 0
        while i > 0:
            res += self.bits[i]
            i -= i & -i
        return res

n = int(input())
a = list(map(int, input().split()))
bits = BIT(n)

count = 0

for i in range(n - 1, -1, -1):
    count += bits.total(a[i] - 1)
    bits.update(a[i], 1)
    
print(count)
