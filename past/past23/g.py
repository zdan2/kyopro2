n,q=map(int,input().split())
a=list(map(int,input().split()))
ca=[0]
for e in a:
    ca.append(ca[-1]+e)
for _ in range(q):
    l,r=map(int,input().split())
    cl=l%n
    cr=r%n
    ll=(l+n-1)//n
    rr=r//n
    print('a',ll,rr,cl,cr)
    
    