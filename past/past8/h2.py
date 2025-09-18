from collections import deque, defaultdict

n,x = map(int,input().split())
d = defaultdict(list)

for _ in range(n-1):
    a, b, c = map(int, input().split())
    d[a].append((b, c))
    d[b].append((a, c))

# 全対距離を格納するための2次元配列
# dist[i][j] = 頂点 i から頂点 j への距離
dist = [[0]*(n+1) for _ in range(n+1)]

def bfs(start):
    # start からの最短距離を求める
    q = deque([start])
    visited = [-1]*(n+1)
    visited[start] = 0

    while q:
        u = q.popleft()
        for nxt, cost in d[u]:
            if visited[nxt] == -1:
                visited[nxt] = visited[u] + cost
                q.append(nxt)
    return visited

# 各頂点を始点に BFS を実行して全対距離を求める
for node in range(1, n+1):
    visited = bfs(node)
    for v in range(1, n+1):
        dist[node][v] = visited[v]

# dist に全頂点対 (i,j) の距離が格納されている
# たとえば、出力例
for e in dist:
    for y in e:
        if y==x:
            print('Yes')
            exit()
print('No')
