mod=998244353
n=int(input())
a=list(map(int,input().split()))
a.sort()
ca=[a[0]]
d=[i*e for i,e in enumerate(a)]
cd=[d[0]]
for i in range(1,n):
    ca.append(ca[-1]+a[i])
    cd.append(cd[-1]+d[i])
r=a[0]*cd[-1]
for i in range(1,n):
   r+=(a[i]*((cd[-1]-cd[i])-(ca[-1]-ca[i])))%mod
   r%=mod
   print('r',i,r)
r+=sum(e*e%mod for e in a)%mod
r%=mod
print(ca)
print(cd)
print(d)
print(r) 