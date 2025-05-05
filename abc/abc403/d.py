def f(nums):
    pp=0
    p=0
    i=1
    while True:
        cur=min(p,pp+x)

from collections import Counter
n,d=map(int,input().split())
ca=Counter(list(map(int,input().split()))).most_common()
ca=sorted(ca,key=lambda x: x[0])
print(ca)
c=0
v=set()
for k,v in ca:
    if k or k+d not in v:
        v.add(k)
        v.add(k+d)
