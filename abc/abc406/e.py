from functools import lru_cache

def count_sum_popcount_up_to(N: int, K: int, MOD: int=None):
    if N < 0:
        return (0, 0)

    bits = bin(N)[2:]
    length = len(bits)
    pow2 = [1]*(length+1)
    if MOD is not None:
        for i in range(1, length+1):
            pow2[i] = (pow2[i-1]*2) % MOD
    else:
        for i in range(1, length+1):
            pow2[i] = pow2[i-1]*2
    
    @lru_cache(None)
    def dfs(pos: int, used: int, less: bool):
        if pos == length:
            if used == K:
                return (1, 0) 
            else:
                return (0, 0)

        limit_bit = int(bits[pos]) 
        res_count = 0
        res_sum = 0

        for bit_sel in [0,1]:
            if (not less) and (bit_sel > limit_bit):
                continue
            
            new_used = used + bit_sel
            if new_used > K:
                continue
            
            new_less = less or (bit_sel < limit_bit)

            sub_count, sub_sum = dfs(pos+1, new_used, new_less)
            if sub_count > 0 and bit_sel == 1:
                add_val = pow2[length-1-pos] 
                if MOD is None:
                    sub_sum += add_val * sub_count
                else:
                    sub_sum = (sub_sum + (add_val % MOD)*sub_count) % MOD

            res_count += sub_count
            if MOD is None:
                res_sum += sub_sum
            else:
                res_count %= MOD
                res_sum   = (res_sum + sub_sum) % MOD

        return (res_count, res_sum)

    c, s = dfs(0,0,False)
    return (c, s)

def count_sum_popcount_range(L: int, R: int, K: int, MOD: int=None):
    if R < 0 or L>R:
        return (0,0)
    
    cR, sR = count_sum_popcount_up_to(R, K, MOD)
    cL, sL = count_sum_popcount_up_to(L-1, K, MOD) if L>0 else (0,0)
    count_ = cR - cL
    sum_   = sR - sL
    if MOD:
        count_ %= MOD
        sum_   %= MOD
    return (count_, sum_)

t=int(input())
mod=998244353
for _ in range(t):
    n,k=map(int,input().split())
    _,s=count_sum_popcount_up_to(n,k,mod)
    print(s)