r=[]
n=int(input())
for i in range(n-1):
    r.append([0 for _ in range(i+1)]+list(map(int,input().split())))
for a in range(n-2):
    for b in range(a,n-1):
        for c in range(b+1,n):
            if r[a][b]+r[b][c]<r[a][c]:
                print('Yes')
                exit()
print('No')