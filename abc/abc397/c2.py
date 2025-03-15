n=int(input())
a=list(map(int,input().split()))
mc=0
for i in range(n):
    ll=len(set(a[:i]))
    rl=len(set(a[i:]))
    mc=max(mc,ll+rl)
print(mc)