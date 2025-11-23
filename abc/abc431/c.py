from collections import deque
n,m,k=map(int,input().split())
h=sorted(map(int,input().split()))
b=sorted(map(int,input().split()))
hq=deque(h)
bq=deque(b)
c=0
while hq and bq:
    if hq[0]<=bq[0]:
        hq.popleft()
        bq.popleft()
        c+=1
    else:
        bq.popleft()
    if c==k:
        print('Yes')
        exit()
print('No')