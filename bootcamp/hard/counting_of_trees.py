from collections import Counter
mod=998244353
n=int(input())
c=Counter(map(int,input().split()))
k=max(c.keys())
r=1
for i in range(k):
    if i not in c:
        print(0)
        exit()
    r*=c[i+1]*c[i]%mod
print(r)