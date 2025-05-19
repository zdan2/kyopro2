n,m=map(int,input().split())
x=[-1]*n
for i in range(m):
    k=int(input())
    for j in range(k):
        aa,bb=map(int,input().split())
        aa-=1
        if aa>=n:
            print('No')
            exit()
        if x[aa]==-1:
            x[aa]=bb
        elif x[aa]!=bb:
            print('No')
            exit()
print(x)