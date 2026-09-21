input()
l=list(map(int,input().split()))
m=sum(l)
c=0
r=m
for e in l:
    c+=e
    r=min(r,abs(m-c-c))
print(r)