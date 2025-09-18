from collections import Counter
n=int(input())
a=list(map(int,input().split()))
ai=[e+i for i,e in enumerate(a)]
aj=[j-e for j,e in enumerate(a)]
ci=Counter(ai)
cj=Counter(aj)
c=0
for k,v in ci.items():
    if k in cj:
        c+=v*cj[k]
print(c)