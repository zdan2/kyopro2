from collections import defaultdict
n=int(input())
t=[tuple(map(int,input().split())) for _ in range(n)]
m=int(input())
d=defaultdict(dict)
r=[]
for k in range(m):
    s=input()
    r.append(s)
    l=len(s)
    for i in range(l):
        if s[i] not in d[(l,i+1)]:
            d[(l,i+1)][s[i]]=[k]
        else:
            d[(l,i+1)][s[i]].append(k)
ans=set()
for j,e in enumerate(r):
    l=len(e)
    if l<n:
        continue
    for i in range(n):
        if e[i] not in d[t[i]]:
            break
        if len(d[t[i]])==1 and d[t[i]][e[i]]==[j]:
            break
    else:
        ans.add(j)
for i in range(m):
    if i in ans:
        print('Yes')
    else:
        print('No')