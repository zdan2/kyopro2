n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
j=0
for i in range(m):
    if a[j]==b[i]:
        j+=1
        if j==n:
            print('Yes')
            exit()
print('No')