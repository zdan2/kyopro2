from collections import defaultdict

n = int(input())
t = [tuple(map(int, input().split())) for _ in range(n)]

m = int(input())
d = defaultdict(dict)
r = []

for k in range(m):
    s = input()
    r.append(s)
    l = len(s)
    for i in range(l):
        if s[i] not in d[(l, i+1)]:
            d[(l, i+1)][s[i]] = [k]
        else:
            d[(l, i+1)][s[i]].append(k)

