from collections import deque
d=[(0,1),(1,2),(2,3),(0,4),(1,5),(2,6),(3,7),(4,5),(5,6),(6,7)]
r=[1,2,3,4,5,6,7,8]
c=0
v=set()
s=list(map(int,input().split()))+list(map(int,input().split()))
q=deque([(s,0)])
b=0
while q:
    a,b=q.popleft()
    if a==r:
        break
    for i,j in d:
        e=a.copy()
        e[i],e[j]=e[j],e[i]
        if tuple(e) in v:
            continue
        v.add(tuple(e))
        q.append((e,b+1))
print(b)