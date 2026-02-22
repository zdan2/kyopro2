from collections import deque
t=int(input())
for _ in range(t):
    n,d=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    q=deque()
    for i in range(n):
        q.append([i,a[i]])
        c=b[i]
        while c>0:
            if q[0][1]>c:
                q[0][1]-=c
                break
            else:
                c-=q[0][1]
                q.popleft()
        if q and q[0][0]<=i-d:
            q.popleft()
    print(sum(r[1] for r in q))