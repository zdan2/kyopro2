n,q=map(int,input().split())
a=list(map(int,input().split()))
ca=[0,a[0]]
for i in range(1,n):
    ca.append(ca[-1]+a[i])
for _ in range(q):
    l,r=map(int,input().split())
    print(ca[r]-ca[l-1])