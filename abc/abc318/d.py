from functools import lru_cache
n=int(input())
mx=[[0]*n for _ in range(n)]
for i in range(n-1):
    a=list(map(int,input().split()))
    for j in range(i+1,n):
        mx[i][j]=a[j-i-1]

full=2**n-1
@lru_cache(None)
def f(mask):
    if mask==full:
        return 0
    
    i=0
    while (mask>>i)&1:
        i+=1
    
    r=f(mask|1<<i)
    for j in range(i+1,n):
        if (mask>>j) & 1:
            continue
        r=max(r,mx[i][j]+f(mask | (1<<i) | (1<<j)))
        
    return r

print(f(0))