n,m=map(int,input().split())
r=[[] for _ in range(m)]
for _ in range(n):
    a,b=map(int,input().split())
    r[a-1].append(b)
for e in r:
    print(sum(e)/len(e))    