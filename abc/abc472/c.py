from collections import deque
n,m,k=map(int,input().split())
a=list(map(int,input().split()))
q=deque()
r=0
for i in range(n):
    if a[i]>k:
        print('No')
        continue
    while q and q[0]<=i-m:
        r-=a[q[0]]
        q.popleft()
    if r+a[i]>k:
        print('No')
    else:
        r+=a[i]
        q.append(i)
        print('Yes')