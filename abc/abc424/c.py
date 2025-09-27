from collections import deque
n=int(input())
d={i:set() for i in range(n+1)}
for i in range(1,n+1):
    a,b=map(int,input().split())
    d[a].add(i)
    d[b].add(i)
q=deque(list(d[0]))
skill=[False]*(n+1)
if q:
    skill[0]=True
else:
    print(0)
    exit()
while q:
    lq=len(q)
    for _ in range(lq):
        e=q.popleft()
        skill[e]=True
        for j in d[e]:
            if not skill[j]:
                q.append(j)
                skill[j]=True
print(sum(skill)-1)