from collections import deque
n,k=map(int,input().split())
a=list(map(int,input().split()))
d={}
c=0
for i in range(n):
    if a[i] not in d:
        d[a[i]]=deque([i])
    else:
        d[a[i]].append(i)
    if i-k>=0:
        b=a[i-k]
        if len(d[b])==1:
            del d[b]
        else:
            d[b].popleft()
    if len(d)==k:
        c+=1
print(c)