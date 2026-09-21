MOD = 998244353
N_MAX = 2 * 10**5

fact = [1] * (N_MAX + 1)
for i in range(1, N_MAX + 1):
    fact[i] = fact[i-1] * i % MOD

inv_fact = [1] * (N_MAX + 1)
inv_fact[N_MAX] = pow(fact[N_MAX], MOD - 2, MOD)  # フェルマーの小定理
for i in range(N_MAX, 0, -1):
    inv_fact[i-1] = inv_fact[i] * i % MOD

def comb(n, k):
    if k < 0 or k > n:
        return 0
    return fact[n] * inv_fact[k] % MOD * inv_fact[n-k] % MOD

n,k=map(int,input().split())
a=list(map(int,input().split()))
sq = sum(e * e for e in a) % MOD
sa = sum(a) % MOD
pair = 0
for e in a:
    sa = (sa - e) % MOD
    pair = (pair + e * sa) % MOD

ans = (comb(n-1, k-1) * sq + 2 * comb(n-2, k-2) * pair) % MOD
print(ans)