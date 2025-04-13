n,k=map(int,input().split())
mod=10**9
if n<k:
    print(1)
    exit()
a=[1]*(n+1)
sa=[0]*(n+1)
sa[0]=a[0]
for i in range(1,k):
    sa[i]=sa[i-1]+a[i]
for i in range(k,n+1):
    a[i]=sa[i-1]-sa[i-k-1]
    sa[i]=(sa[i-1]+a[i])%mod
print(a[n]%mod)