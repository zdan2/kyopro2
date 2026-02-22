n=int(input())
a=list(map(int,input().split()))
d={}
for e in a:
    if e-1 in d:
        d[e]=d[e-1]+1
    else:
        d[e]=1
r=0
for _,v in d.items():
    r=max(r,v)
print(r)