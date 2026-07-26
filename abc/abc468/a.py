n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(1,n-1):
    c+=a[i-1]<a[i]>a[i+1]
print(c)