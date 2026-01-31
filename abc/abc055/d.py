from collections import deque
dq=deque()
n=int(input())+2
s=list(input())
s+=[s[0],s[1]]
dq.append(['S','S'])
dq.append(['S','W'])
dq.append(['W','W'])
dq.append(['W','S'])
r=[]
while dq:
    t=dq.popleft()
    l=len(t)
    if len(t)==n:
        r.append(t)
        continue
    if t[-1]=='S' and s[l-1]=='o':
        if t[-2]=='S':
            t.append('S')
        elif t[-2]=='W':
            t.append('W')
        
    elif t[-1]=='S' and s[l-1]=='x':
        if t[-2]=='S':
            t.append('W')
        elif t[-2]=='W':
            t.append('S')
    
    elif t[-1]=='W' and s[l-1]=='o':
        if t[-2]=='S':
            t.append('W')
        elif t[-2]=='W':
            t.append('S')
    
    elif t[-1]=='W' and s[l-1]=='x':
        if t[-2]=='S':
            t.append('S')
        elif t[-2]=='W':
            t.append('W')
            
    dq.append(t)
for e in r:
    if e[-1]==e[1] and e[-2]==e[0]:
        print(''.join(e[:-2]))
        exit()
print(-1)