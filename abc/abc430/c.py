from collections import deque
n,a,b=map(int,input().split())
s=list(input())
l=0
cb=0
ans=0
q=deque()
for r in range(n):
    if s[r]=='a':
        q.append(r)
    else:
        cb+=1
    while cb>=b:
        if s[l]=='a':
            if q and q[0]==l:
                q.popleft()
        else:
            cb-=1
        l+=1
    if len(q)>=a:
        ans+=q[-a]-l+1
print(ans)