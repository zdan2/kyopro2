n,q=map(int,input().split())
mod=1000000007
a=list(map(int,input().split()))
c=list(map(int,input().split()))
c=[1]+c+[1]
pr=[0]
r=0
for i in range(n-1):
    pr.append((pr[-1]+pow(a[i],a[i+1],mod))%mod)
for i in range(q+1):
    s=min(c[i],c[i+1])-1
    g=max(c[i],c[i+1])-1
    r+=(pr[g]-pr[s])%mod
print(r%mod)