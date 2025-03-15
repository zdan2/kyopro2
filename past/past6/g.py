from collections import defaultdict
n,m,q=map(int,input().split())

d=defaultdict(list)

for _ in range(m):
    a,b,c=map(int,input().split())
    d[a].append((b,c))
    d[b].append((a,c))

x=list(map(int,input().split()))
v=set()
r=set()
stack=[(1,0)]
for i,j in d[1]:
    stack.append((i,j))
can=[]
for xi in x:
    can=[]
    while stack:
        now,nw=stack.pop()
        #print(now,nw,v,xi)
        if (now,nw) not in v and nw<=xi:
            v.add((now,nw))
            r.add(now)
            for nxt,w in d[now]:
                if w<=xi:
                    can.append((nxt,w))
                else:
                    can.append((nxt,w))
        else:
            can.append((now,nw))
    stack=can
    print(len(r))