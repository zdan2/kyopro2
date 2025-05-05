n=int(input())
mx=[list(input()) for _ in range(n)]
tx=[list(input()) for _ in range(n)]
r=[]
for k in range(4):
    c=0
    for i in range(n):
        for j in range(n):
            if mx[i][j]!=tx[i][j]:
                c+=1
    r.append(c+k)
    mx=[row for row in zip(*mx[::-1])]
print(min(r))