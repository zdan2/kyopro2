from collections import deque,defaultdict
q=int(input())
dq=deque()
for i in range(q):
    x=input().split()
    if x[0]=='1':
        dq.append((x[1],int(x[2])))
    if x[0]=='2':
        dd=defaultdict(int)
        d=int(x[1])
        while d>0 and dq:
            e,en=dq.popleft()
            if d>en:
                d-=en
                dd[e]+=en
            else:
                dd[e]+=d
                dq.appendleft((e,en-d))
                d=0
        c=0
        for v in dd.values():
           c+=v*v
        print(c)        