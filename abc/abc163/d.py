n,k=map(int,input().split())
c=0
mod=10**9+7
for i in range(k,n+2):
    small=(i*(i-1))//2
    large=(i*(2*n-i+1))//2
    c+=large-small+1
    c%=mod
print(c)