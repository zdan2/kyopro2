from collections import deque,defaultdict

n,m,l,s,t=map(int,input().split())
d=defaultdict(list)
for _ in range(m):
    u,v,c=map(int,input().split())
    d[u].append((v,c))
q=deque([(1,0,0)])
can=set()
while q:
    cp,cc,ct=q.popleft()
    if ct==l and s<=cc<=t:
        can.add(cp)
        continue
    elif ct>=l:
        continue
    for nxt,nc in d[cp]:
        if cc+nc<=t:
            q.append((nxt,cc+nc,ct+1))
print(*sorted(can))