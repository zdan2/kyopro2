n=int(input())
s=list(input())
a=[i for i,e in enumerate(s) if e=='A']
b=[i for i,e in enumerate(s) if e=='B']
c=[i*2 for i in range(n)]
r1=sum(abs(x-y) for x,y in zip(a,c))
r2=sum(abs(x-y) for x,y in zip(b,c))
print(min(r1,r2))