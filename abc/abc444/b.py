n,k=map(int,input().split())
c=0
for i in range(n+1):
    a=i
    r=0
    while a>0:
       r+=a%10
       a//=10
    if r==k:
        c+=1
print(c) 