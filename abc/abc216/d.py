from collections import deque,defaultdict

n,m=map(int,input().split())
s=defaultdict()
r=deque()
for _ in range(m):
    k=int(input())
    a=list(map(int,input().split()))
    dq=deque(a)
    r.append(dq)

while r:
    x=r.popleft()
    a=x[0]
    while a in s:
        s[a].popleft()
        x.popleft()
        if s[a]:
            r.appendleft(s[a])
        del s[a]
        if x:
            a=x[0]
        else:
            break
    if x:
        s[x[0]]=x        

print('No' if r or s else 'Yes')     