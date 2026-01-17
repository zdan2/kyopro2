from collections import defaultdict
da=defaultdict(int)
db=defaultdict(int)
n=int(input())
for i in range(1,n+1):
    a,b=map(int,input().split())
    da[i]=a
    db[i]=b
c=0
for i in range(1,n+1):
    j=da[i]
    if db[i]==db[j]:
        c+=1
print(c//2)