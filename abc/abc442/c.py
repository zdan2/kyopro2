def c(a):
    if a<3:
        return 0
    return a*(a-1)*(a-2)
n,m=map(int,input().split())
d={i:{i} for i in range(1,n+1)}
for _ in range(m):
    a,b=map(int,input().split())
    d[a].add(b)
    d[b].add(a)
r=[c(n-len(x))//6 for k,x in d.items()]
print(*r)