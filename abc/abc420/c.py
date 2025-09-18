n,q=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
s=sum(min(i,j) for (i,j) in zip(a,b))
for _ in range(q):
    c,*r=input().split()
    idx,m=int(r[0])-1,int(r[1])
    pa=a[idx]
    pb=b[idx]
    if c=='A':
        a[idx]=m
    else:
        b[idx]=m
    d=min(a[idx],b[idx])-min(pa,pb)
    s+=d
    print(s)