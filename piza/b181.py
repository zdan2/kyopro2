n,m=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
d=[list(map(int,input().split())) for _ in range(m)]
d.sort()
c=0
while a and d:
   price=a.pop()
   dis,rem=d[-1]
   c+=max(0,price-dis)
   d[-1][1]-=1
   if d[-1][1]==0:
       d.pop()
print(c+sum(a))