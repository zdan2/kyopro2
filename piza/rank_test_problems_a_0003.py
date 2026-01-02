a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=float('inf')
for i in range(3):
    c=min(c,a[i]+b[i])
print(c)