from collections import deque
n,k=map(int,input().split())
a=list(map(int,input().split()))
r=sorted([e%k for e in a])
q=deque(r)
c=float('inf')
for i in range(n):
    c=min(c,q[-1]-q[0])
    b=q.popleft()
    q.append(b+k)
print(c)