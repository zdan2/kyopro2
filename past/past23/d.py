a=list(input().split())
h=int(a[0])
w=int(a[1])
c1=a[2]
c2=a[3]
s=[list(input()) for _ in range(h)]
dyx=[(1,0),(0,1),(-1,0),(0,-1)]
for i in range(h):
    for j in range(w):
        if s[i][j]==c1:
            for dy,dx in dyx:
                ny=i+dy
                nx=j+dx
                if 0<=ny<h and 0<=nx<w and s[ny][nx]==c2:
                    print('Yes')
                    exit()
print('No')