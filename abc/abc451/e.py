n=int(input())
r=[]
for i in range(n-1):
    r.append([0]*(i+1)+list(map(int,input().split())))
r.append([0]*n)
for k in range(1,n):
    h=False
    for i in range(n-1):
        for j in range(n):
            if i>=j or k==j or k==i:
                continue
            if r[i][k]+r[k][j]==r[i][j]:
                if r[i][j]==0:
                    r[j][i]=r[i][j]
                    h=True
                if r[k][i]==0:
                    r[k][i]=r[i][k]
                elif r[k][i]!=r[i][k]:
                    h=False
                if r[j][k]==0:
                    r[j][k]=r[k][j] 
                elif r[j][k]!=r[k][j]:
                    h=False
                break
    if not h:
        print('No')
        exit()
print('Yes')