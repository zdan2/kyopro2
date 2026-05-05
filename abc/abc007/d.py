from functools import lru_cache
a,b=map(int,input().split())

def f(n):
    digits=list(map(int,str(n)))
    n=len(digits)
    @lru_cache(maxsize=None)
    def dp(p,t):
        if p==n:
            return 1
        limit=digits[p] if t else 9
        result=0
        for d in range(limit+1):
            if d==4 or d==9:
                continue
            nt=t and d==limit
            result+=dp(p+1,nt)
        return result
    return dp(0,True)-1
total=b-a+1
safe=f(b)-f(a-1)
print(total-safe)