n,m,k=map(int,input().split())
a=list(map(int,input().split()))
c=0
for i in range(1,2**m):
    if i.bit_count()!=k:
        continue
    s=0
    for j in range(i.bit_length()):
        if i>>j&1:
            s+=a[j]
    if s%n==0:
        c+=1
print(c)