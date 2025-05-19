n=int(input())
a=list(map(int,input().split()))
ca=[a[0]]
for i in range(1,n):
    ca.append(ca[-1]+a[i])
r=0
for i in range(n-1):
   r+=a[i]*(ca[-1]-ca[i]) 
print(r)