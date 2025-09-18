def comb(n, r, mod):
    if r < 0 or r > n:
        return 0
    r = min(r, n - r)
    num = 1
    den = 1
    for i in range(r):
        num = (num * (n - i)) % mod
        den = (den * (i + 1)) % mod
    return (num * pow(den, mod-2, mod)) % mod
mod=10**9+7
n,a,b=map(int,input().split())
vn=(pow(2,n,mod)-1)%mod
va=comb(n,a,mod)
vb=comb(n,b,mod)
print((vn-va-vb)%mod)