from collections import Counter
n=int(input())
d=list(map(int,input().split()))
c=Counter(d)
mod=998244353
if c[0]!=1:
    print(0)
    exit()
r=1
for e in d[1:]:
    r*=c[e-1]
    r%=mod
print(r)