from collections import deque
n=int(input())
s=input()
h=0
q=deque()
i=1
q.append(i)
for e in s[1:]:
    i+=1
    if e=='o':
        if h:
           q.append(i)
        else:
            q.appendleft(i)
        h=1-h
    else:
        if h:
            q.append(i)
        else:
            q.appendleft(i)
if h:
    print(*q)
else:
    q=list(q)[::-1]
    print(*q)