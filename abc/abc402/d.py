from collections import defaultdict
n,m=map(int,input().split())
d=defaultdict(int)
for _ in range(m):
    a,b=map(int,input().split())
    d[(a+b)%n]+=1
c=0
for _,v in d.items():
    c+=(m-v)*v
print(c//2)