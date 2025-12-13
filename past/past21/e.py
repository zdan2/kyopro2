n,m=map(int,input().split())
d={}
for _ in range(n):
    a,b,c=map(int,input().split())
    d[(a,b)]=c
    d[(b,a)]=c
x=list(map(int,input().split()))
s=x[0]
for e in x[1:]:
    if (s,e) in d:
        s=d[(s,e)]
    else:
        s+=e
print(s)