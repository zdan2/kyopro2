n,k=map(int,input().split())
r=list(map(int,input().split()))
r.sort()
a=r[-k:]
c=0
for e in a:
    c=(c+e)/2
print(c)