n,m=map(int,input().split())
a=[0]*(n+1)
for _ in range(m):
    l,r=map(int,input().split())
    a[l-1]+=1
    a[r]-=1
c=[a[0]]
for e in a[1:n]:
    c.append(c[-1]+e)
print(min(c))