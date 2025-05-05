mod = 10**9 + 7

# n の最大値（問題等で必要な範囲に合わせて調整）
n,a,b=map(int,input().split())

# 階乗とその逆元を格納する配列を作る
fact = [1] * (n + 1)       # fact[i] = i! (mod mod)
inv_fact = [1] * (n + 1)   # inv_fact[i] = (i!)^(-1) (mod mod)

def prepare_factorials():
    # 1. fact（階乗）を前計算
    for i in range(1, n + 1):
        fact[i] = fact[i - 1] * i % mod
    
    # 2. inv_fact（階乗の逆元）を前計算
    #    (n!)^(-1) をまず pow で求めてから、降順に使い回す手法
    inv_fact[n] = pow(fact[n], mod - 2, mod)  # フェルマーの小定理で逆元を計算
    for i in range(n - 1, 0, -1):
        inv_fact[i] = inv_fact[i + 1] * (i + 1) % mod
    # 0! = 1 の逆元は1と分かっているので明示的に入れておく
    inv_fact[0] = 1

def comb(n, r):
    if r < 0 or r > n:
        return 0
    return fact[n] * inv_fact[r] % mod * inv_fact[n - r] % mod

v=pow(2,n,mod)
ans=(v-1)%mod-comb(n,a)-comb(n,b)
print(ans)