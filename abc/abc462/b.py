n=int(input())
r=[[] for _ in range(n)]
for i in range(n):
    e=list(map(int,input().split()))
    for j in e[1:]:
        r[j-1].append(i+1)
for l in r:
    print(len(l),*l)