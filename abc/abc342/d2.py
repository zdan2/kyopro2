from collections import Counter
m=int(input())
a=list(map(int,input().split()))
sqrt=int(max(a)**0.5)+1
er=[True]*(sqrt+1)
er[0]=False
for i in range(2,sqrt):
    if er[i]==True:
        for j in range(i*i,sqrt,i):
            er[j]=False
b=[]
for i,h in enumerate(er):
   if h:
       b.append(i*i)
c=[]
for e in a:
    if e==0:
        c.append(0)
        continue
    n=e
    for f in b[1:]:
        if f>n:
            break
        while True:
            if n%f==0:
                n//=f
            else:
                break
    c.append(n)
cc=Counter(c)
a=0
for k,v in cc.items():
    if k==0:
        a+=v*m-(v+1)*v//2
    else:
        a+=v*(v-1)//2
print(a) 