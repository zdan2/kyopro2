from collections import Counter
n,m=map(int,input().split())
s=[list(input()) for _ in range(n)]
ts=[r for r in zip(*s)]
c=[0]*n
for e in ts:
    w=Counter(e).most_common()[-1][0]
    for i in range(n):
        if e[i]==w:
            c[i]+=1
r=max(c)
a=[]
for i,e in enumerate(c):
    if e==r:
        a.append(i+1)
print(*a)