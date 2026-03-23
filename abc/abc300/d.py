from collections import defaultdict
from bisect import bisect
def er(n):
    sqrt=int(n**0.5)+1
    f=[True]*sqrt
    f[0]=False
    f[1]=False
    for i in range(2,sqrt):
        if f[i]:
            for j in range(i+i,sqrt,i):
                f[j]=False
        
    return [i for i,e in enumerate(f) if e]

n=int(input())
r=er(n)
c=0
for i in range(len(r)-2):
    for j in range(i+1,len(r)-1):
        t=n/(r[i]*r[i])
        t/=r[j]
        t**=0.5
        idx=bisect(r,t)-1
        if idx>j:
            c+=idx-j
        else:
            break
print(c)        
