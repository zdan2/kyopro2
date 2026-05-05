n=int(input())
mx=[list(input()) for _ in range(n)]
for i in range(n-1):
    for j in range(n-1):
        if mx[i][j+1]=='?' and mx[i+1][j]=='?':
            mx[i+1][j]='0'
            mx[i][j+1]='0'
        elif mx[i+1][j]=='?' or mx[i][j+1]=='?':
            if mx[i+1][j]=='?':
                mx[i+1][j]=mx[i][j+1]
            else:
                mx[i][j+1]=mx[i+1][j]
        else:
            print(-1)
            exit()
    print(mx[i])
for r in mx:
    print(r)