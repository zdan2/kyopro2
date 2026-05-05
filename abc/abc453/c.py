from collections import deque
n=int(input())
l=list(map(int,input().split()))
q=deque()
q.append([0.5,0])
r=0
for e in l:
    nq=deque()
    while q:
        cur,c=q.popleft()
        if cur>0 and cur-e<0:
            nq.append([cur-e,c+1])
            nq.append([cur+e,c])
            r=max(r,c+1)
        elif cur<0 and cur+e>0:
            nq.append([cur+e,c+1])
            nq.append([cur-e,c])
            r=max(r,c+1)
        else:
            nq.append([cur+e,c])
            nq.append([cur-e,c])
    q=nq
print(r)