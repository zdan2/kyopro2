from sortedcontainers import SortedSet
n,k=map(int,input().split())
a=list(map(int,input().split()))
s=SortedSet(a)
for i in range(k):
    p=s.pop(0)
    for e in a:
        s.add(p+e)
print(p)    