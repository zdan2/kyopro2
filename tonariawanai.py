from collections import defaultdict,deque
n=int(input())
dp=[[0]*2 for _ in range(n)]
parent=[-1]*n
a=list(map(int,input().split()))
d=defaultdict(list)
for _ in range(n-1):
    u,v=map(int,input().split())
    u-=1
    v-=1
    d[u].append(v)
    d[v].append(u)
q=deque([(0,0)])
dl=defaultdict(list)
dl[0]=[0]
max_l=0
seen={0} 
while q:
    cp,cl=q.popleft()
    for nxt in d[cp]:
        if nxt in seen:
            continue
        seen.add(nxt)
        parent[nxt]=cp
        dl[cl+1].append(nxt)
        max_l=max(max_l,cl+1)
        q.append((nxt,cl+1))
for cur_lv in range(max_l,-1,-1):
    for node in dl[cur_lv]:
        dp[node][1]=a[node]
        for child in d[node]:
            if child==parent[node]:
                continue
            dp[node][0]+=max(dp[child][0],dp[child][1])
            dp[node][1]+=dp[child][0]
print(max(dp[0]))