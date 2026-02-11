from collections import deque
n=int(input())
s=list(input())+['.','.']
t=list(input())+['.','.']
seen=set()
q=deque()
q.append((s,0))
seen.add(tuple(s))
while q:
    a,count=q.popleft()
    if a==t:
        print(count)
        exit()
    didx=a.index('.')
    for i in range(n+1):
        b=a.copy()
        if b[i]!='.' and b[i+1]!='.':
            b[didx],b[didx+1]=b[i],b[i+1]
            b[i],b[i+1]='.','.'
            if tuple(b) not in seen:
                q.append((b,count+1))
                seen.add(tuple(b))
print(-1)