r=[]
def f(n,m,s=[]):
    if m==0:
        r.append(s)
        return
    if s:
        e=s[-1]
    else:
        e=0
    for x in range(e+1,n+1):
        y=s.copy()
        y.append(x)
        f(n,m-1,y)
n,m=map(int,input().split())
f(m,n)
for e in r:
    print(*e)