from itertools import combinations
n,m=map(int,input().split())
ex=set()
can=set()
for _ in range(m):
    a,b,c=map(int,input().split())
    ex.add((a,b,c))
ma=0
l=list(range(1,n+1))
for i in range(2,n+1):
    for ca in combinations(l,i):
        aa=set()
        ca=set(ca)
        for e in ex:
            e=set(e)
            if len(e&ca)==2:
                aa.add(*(e-ca))
        ma=max(ma,len(aa))
print(ma)