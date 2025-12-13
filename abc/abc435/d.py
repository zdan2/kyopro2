from collections import deque,defaultdict
n,m=map(int,input().split())
d=defaultdict(list)
for _ in range(m):
    u,v=map(int,input().split())
    d[v].append(u)
k=int(input())
q=deque()
can=set()
for _ in range(k):
    op,t=map(int,input().split())
    if op==1:
        if t in can:
            continue
        q.append(t)
        can.add(t)
        while q:
            cur=q.popleft()
            for nxt in d[cur]:
                if nxt not in can:
                    can.add(nxt)
                    q.append(nxt)
    else:
        print('Yes' if t in can else 'No')