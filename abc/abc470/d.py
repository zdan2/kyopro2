n,q=map(int,input().split())
p=list(map(int,input().split()))
p=[e-1 for e in p]
inv=[0]*n
for i,e in enumerate(p):
    inv[e]=i
for _ in range(q):
    s=input().split()
    if s[0]=='1':
        x=int(s[1])-1
        y=int(s[2])-1
        a=p[x]
        b=p[y]
        p[x],p[y]=b,a
        inv[a]=y
        inv[b]=x
    else:
        p,inv=inv,p
p=[e+1 for e in p]
print(*p)