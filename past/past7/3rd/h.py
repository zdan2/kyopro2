from collections import deque
n=int(input())
k=n-2
a=sum(map(int,input().split()))
h=1
q=deque()
while a:
    r=(a+(k-1))//k
    if h:
        q.append(r)
        h=0
    else:
        q.appendleft(r)
        h=1
    k-=1
    a-=r
q.append(0)
py=0
r=0
while q:
    y=q.popleft()
    r+=(1+(y-py)**2)**0.5
    py=y
print(r)