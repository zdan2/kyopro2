n=int(input())
m=int(input())
f=[set() for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    f[a].add(b)
    f[b].add(a)
s=f[1]
sc=f[1].copy()
for e in s:
    sc|=f[e]
sc.discard(1)
print(len(sc))