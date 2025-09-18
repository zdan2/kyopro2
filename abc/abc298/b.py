n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]
b=[list(map(int,input().split())) for _ in range(n)]
for _ in range(4):
    h=True
    for i in range(n):
        for j in range(n):
            if a[i][j]==1:
                if b[i][j]==0:
                    h=False
                    break
        if not h:
            break
    if h:
        print('Yes')
        exit()
    a=[list(r) for r in zip(*a[::-1])]
print('No')