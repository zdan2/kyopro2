import sys
sys.setrecursionlimit(10**7)
t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    d={i:[i] for i in range(n)}
    for _ in range(m):
        u,v=map(int,input().split())
        d[u-1].append(v-1)
        d[v-1].append(u-1)
    w=int(input())
    week=[input() for _ in range(n)]
    colors=[[0]*w for _ in range(n)]
    def dfs(day,cur):
        if colors[cur][day]==1:
            return True
        if colors[cur][day]==2:
            return False
        colors[cur][day]=1
        nd=(day+1)%w
        for nxt in d[cur]:
            if week[nxt][nd]=='o':
                if dfs(nd,nxt):
                    return True
        colors[cur][day]=2
        return False
    for i in range(n):
        if week[i][0]=='o':
            if dfs(0,i):
                print('Yes')
                break
    else:
        print('No')