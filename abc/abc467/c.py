n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
ca=a.copy()
car=ca[::-1]
br=b[::-1]
r1=float('inf')
cca=a.copy()
cca[0]+=1
for i in range(n-1):
    if (cca[i]+cca[i+1])%m!=b[i]:
        cca[i+1]+=1
r1=sum(cca)-sum(a)
r2=float('inf')
ccar=car.copy()
ccar[0]+=1
for i in range(n-1):
    if (ccar[i]+ccar[i+1])%2!=br[i]:
        ccar[i+1]+=1
r2=sum(ccar)-sum(a)
for i in range(n-1):
    if (ca[i]+ca[i+1])%2!=b[i]:
        ca[i+1]+=1
    if (car[i]+car[i+1])%2!=br[i]:
        car[i+1]+=1
r3=sum(ca)-sum(a)
r4=sum(car)-sum(a)
print(min(r1,r2,r3,r4))