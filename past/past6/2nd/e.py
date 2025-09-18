from collections import deque
q=deque()
n=int(input())
s=input()
d={'A':(1,0),'B':(1,1),'C':(1,2),'D':(-1,0),'E':(-1,1),'F':(-1,2),'L':(0,1),'R':(0,-1)}
for i in range(n):
    f=0
    g=0
    a,b=d[s[i]]
    if a==0:
        if b==1:
            q.appendleft(i+1)
        else:
            q.append(i+1)
    if a==1:
        if len(q)<=b:
            f=1
        else:
            q2=deque()
            for _ in range(b):
                c=q.popleft()
                q2.append(c)
            g=q.popleft()
            for _ in range(b):
                c=q2.pop()
                q.appendleft(c)
    if a==-1:
        if len(q)<=b:
            f=1
        else:
            q2=deque()
            for _ in range(b):
                c=q.pop()
                q2.append(c)
            g=q.pop()
            for _ in range(b):
                c=q2.pop()
                q.append(c) 
    if f==0 and g>0:
        print(g)
    if f==1:
        print('ERROR')