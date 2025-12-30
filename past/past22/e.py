n,m=map(int,input().split())
a=list(map(int,input().split()))
d={e:i for i,e in enumerate(a)}
r=0
b=list(map(int,input().split()))
cp=b[0]
for e in b[1:]:
   r+=abs(d[cp]-d[e])
   cp=e
print(r) 