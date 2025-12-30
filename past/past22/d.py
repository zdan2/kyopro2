from itertools import combinations, permutations
n=int(input())
s=[input() for _ in range(n)]
for e in combinations(s,3):
    if any(a+b==c for a,b,c in permutations(e)):
        print('Yes')
        exit()
print('No')