h,w=map(int,input().split())
q=int(input())
mx=[[[0,0,0] for _ in range(w+1)]for _ in range(h+1)]
x=[list(input()) for _ in range(h)]
for i in range(h):
    for j in range(w):
        if x[i][j]=='J':
            x[i][j]=0
        elif x[i][j]=='O':
            x[i][j]=1
        else:
            x[i][j]=2
mx[1][1]=[1,0,0]
for j in range(2,w+1):
    mx[1][j][x[0][j-1]]+=1
for i in range(2,h+1):
    mx[i][1][x[i-1][0]]+=1
for i in range(1,h+1):
    for j in range(1,w+1):
        mx[i][j]=[i+j-k for i,j,k in zip(mx[i-1][j],mx[i][j-1],mx[i-1][j-1])]
        mx[i][j][x[i-1][j-1]]+=1
for _ in range(q):
    a,b,c,d=map(int,input().split())
    print(*[i-j-k+l for i,j,k,l in zip(mx[c][d],mx[c][b-1],mx[a-1][d],mx[a-1][b-1])])