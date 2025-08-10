from collections import deque
n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
q=deque(sorted(b))
r=[]
for i in range(n):
    if q:
        if a[i]<q[0]:
            r.append(a[i])
        while q and a[i]>q[0]:
            q.popleft()
        if a[i]==q[0]:
            q.popleft()
    else:
        r.append(a[i])
print(*r)