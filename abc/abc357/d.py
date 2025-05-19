mod=998244353
n=int(input())
r=0
for i in range(n-1,-1,-1):
    p=pow(10,i,mod)
    r+=n*p%mod
    r%=mod
print(r)
    