from collections import deque
q=int(input())
a=deque()
for _ in range(q):
    op,*b=map(int,input().split())
    if op==1:
        a.append(b)
    if op==2:
        k=b[0]
        r=0
        while a:
            c,x=a.popleft()
            if c<=k:
                k-=c
                r+=x*c
            elif c>k:
                r+=x*k
                a.appendleft([c-k,x])
                break
        print(r)