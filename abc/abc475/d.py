N = 10**7
er = [True] * N
er[0] = er[1] = False
for p in range(2, int(N**0.5) + 1):
    if er[p]:
        for i in range(p*p, N, p):
            er[i] = False
primes = [i for i, prime in enumerate(er) if prime]

d = {}
for p in primes:
    s = str(p)
    r = {}
    for i, c in enumerate(s):
        r.setdefault(c, set()).add(i)
    ss = frozenset(frozenset(v) for v in r.values())
    d.setdefault(len(s), {}).setdefault(ss, []).append(s)

t=input()
td={}
r={}
for i,c in enumerate(t):
        r.setdefault(c, set()).add(i)
ss = frozenset(frozenset(v) for v in r.values())
print(d[len(t)][ss][0] if ss in d[len(t)] else -1)