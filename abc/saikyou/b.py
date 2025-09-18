h,w=map(int,input().split())
s=[list(input()) for _ in range(h)]
dyx=[(0,1),(1,0),(-1,0),(0,-1)]
for i in range(h):
    for j in range(w):
        if s[i][j]=='.':
            continue
        c=0
        for dy,dx in dyx:
            ny=i+dy
            nx=j+dx
            if 0<=ny<h and 0<=nx<w and s[ny][nx]=='#':
                c+=1
        if c%2==1 or c==0:
            print('No')
            exit()
print('Yes')