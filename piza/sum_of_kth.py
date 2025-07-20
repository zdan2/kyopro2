n,k=map(int,input().split())
a=list(map(int,input().split()))
ca=[0]
for i in range(n):
    ca.append(ca[-1]+a[i])
for i in range(n-k+1):
    print(ca[k+i]-ca[i])