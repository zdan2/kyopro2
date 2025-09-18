n,m=map(int,input().split())
a=list(map(int,input().split()))
ca=[a[0]]
for i in range(1,n):
    ca.append((ca[i-1]+a[i])%m)
print(ca)