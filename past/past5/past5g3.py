from collections import defaultdict

h,w=map(int,input().split())
mx=[list(input()) for _ in range(h)]
dyx=[(1,0),(0,1),(-1,0),(0,-1)]
g=defaultdict(list)
for i in range(h):
    for j in range(w):
        if mx[i][j]=='#':
            for dy,dx in dyx:
                y=i+dy
                x=j+dx
                if 0<=y<h and 0<=x<w and mx[y][x]=='#':
                    g[(i+1,j+1)].append((y+1,x+1))

longest_route = []
for i in range(h):
    for j in range(w):
        if mx[i][j]=='#':
            route=[[(i+1,j+1)]]
            while route:
                cur_route = route.pop()
                now = cur_route[-1] 
                if len(cur_route) > len(longest_route): 
                    longest_route = cur_route
                for nxt in g[now]:
                    if nxt not in cur_route: 
                        route.append(cur_route + [nxt])

print(len(longest_route)) 
for a, b in longest_route:
    print(a, b) 

