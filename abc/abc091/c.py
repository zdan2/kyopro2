from collections import defaultdict
n=int(input())
a=[tuple(map(int,input().split())) for _ in range(n)]
b=[tuple(map(int,input().split())) for _ in range(n)]
d=defaultdict(list)

for i in range(n):
    ay,ax=a[i]
    for j in range(n):
        by,bx=b[j]
        if ay<by and ax<bx:
            d[i].append(j)

match=[-1]*n

def dfs(u):
    for v in d[u]:
        if v in visited:
            continue
        visited.add(v)
        if match[v]==-1 or dfs(match[v]):
            match[v]=u
            return True
    return False
c=0
for i in range(n):
    visited=set()
    if dfs(i):
        c+=1
print(c) 