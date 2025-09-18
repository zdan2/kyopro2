from itertools import combinations,permutations
n=int(input())
k=int(input())
cards=[input() for _ in range(n)]
cc=[list(e) for e in combinations(cards,k)]
s=set()
for e in cc:
    r=[''.join(f) for f in permutations(e,k)]
    for l in r:
        s.add(l)
print(len(s))