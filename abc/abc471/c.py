from collections import deque
l=deque()
r=deque()
n=int(input())
a=sorted(list(map(int,input().split())))
for e in a:
    if e<=0:
        l.append(e)
    else:
        r.append(e)
c=0
cur=0
while l or r:
    left=l[-1] if l else -float('inf')
    right=r[0] if r else float('inf')
    if cur-left<=right-cur:
        c+=cur-left
        cur=l.pop()
    else:
        c+=right-cur
        cur=r.popleft()
print(c)