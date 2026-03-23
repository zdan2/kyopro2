def er(n):
    f=[True]*(n+1)
    f[0]=False
    f[1]=False
    for i in range(2,n+1):
        if f[i]:
            for j in range(i+i,n+1,i):
                f[j]=False
    return [i for i,e in enumerate(f) if e]
n=int(input())
a=list(map(int,input().split()))
prime=er(int(max(a)**0.5)+1)
def f(n):
    factors=set()
    if n==0:
        return{-1}
    if n==1:
        return{0}
    for x in prime:
        if x*x>n:
            break
        c=0
        while n%x==0:
            c^=1
            n//=x
        if c:
            factors.add(x)
    if n>1:
        factors.add(n)
    return factors
odd_f=[f(e) for e in a]
d={(0):0}
r=0
for e in odd_f:
    if e=={-1}:
        r+=n-1
    if e=={0}:
        r+=d[(0)]
        d[(0)]+=1
        continue
    y=tuple(sorted(e))
    if y not in d:
        d[y]=1
    else:
        r+=d[y]
        d[y]+=1
print(r)