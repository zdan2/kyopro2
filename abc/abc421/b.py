def f(n,memo):
    if n in memo:
        return memo[n]
    memo[n]=int(str(f(n-1,memo)+f(n-2,memo))[::-1])
    return memo[n]
x,y=map(int,input().split())
print(f(10,{1:x,2:y}))