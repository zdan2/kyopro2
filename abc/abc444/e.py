from sortedcontainers import SortedSet
from collections import deque

n, d = map(int, input().split())
a = list(map(int, input().split()))

l = 0
ss = SortedSet()
q = deque()
res_range = (0, 0)
ans = []
for r in range(n):
    def can_add(val):
        if not ss: return True
        idx = ss.bisect_left(val)
        if idx < len(ss) and ss[idx] < val + d:
            return False
        if idx > 0 and ss[idx-1] > val - d:
            return False
        return True

    while not can_add(a[r]):
        ss.remove(a[l])
        l += 1
    
    ss.add(a[r])
    if l != r:
        ans.append((l, r))
c = n
for l,r in ans:
    c += r - l
print(c)