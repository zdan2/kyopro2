from math import lcm
mod=998244353
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    la=[a[0]]
    for i in range(1,n):
        la.append(lcm(la[-1],a[i]))
    ra=[a[-1]]
    for i in range(n-2,-1,-1):
        ra.append(lcm(ra[-1],a[i]))
    ra=ra[::-1]
    r=[0]*n
    r[0]=ra[1]%mod
    r[-1]=la[-2]%mod
    for i in range(1,n-1):
        r[i]=lcm(la[i-1],ra[i+1])%mod
    print(*r)