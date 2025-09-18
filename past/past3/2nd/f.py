from collections import Counter
n=int(input())
a=[]
for _ in range(n):
    a+=list(input())
m=n
half=m//2
c=Counter(a).most_common()
ca=[x[1]//2*2 for x in c if x[1]>1]
if sum(ca)<m-m%2:
    print(-1)
    exit()
s=''
for i in range(len(ca)):
    take=min(c[i][1]//2,half)
    s+=c[i][0]*take
    half-=take
    if half==0:
        break
center=''
if m%2==1:
    for x,y in c:
        if y%2==1:
            center=x
print(s+center+s[::-1])