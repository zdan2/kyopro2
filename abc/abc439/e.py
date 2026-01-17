n=int(input())
a=[tuple(map(int,input().split())) for _ in range(n)]
b=[]
for x,y in a:
    b.append(x)
    b.append(y)
b.sort()
d={}
for i,e in enumerate(b):
    d[e]=i+1
c=[(d[x],d[y]) for x,y in a]

a=sorted(c,key=lambda x:[x[0],x[-1]])
print(a)
pl=a[0][0]
pr=a[0][1]
c=1
for l,r in a[1:]:
    if pl<l and pr<r:
        c+=1
    pl=l
    pr=r
print(c) 
    