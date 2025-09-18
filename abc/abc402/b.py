from collections import deque
q=deque()
n=int(input())
for _ in range(n):
    d=list(map(int,input().split()))
    if d[0]==1:
        q.append(d[1])
    else:
        print(q.popleft())