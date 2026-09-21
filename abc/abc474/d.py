n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
for i in range(n):
    if a[i]>b[i]:
        w=[1]*n
        w[i]=10**18
        print('Yes')
        print(*w)
        exit()
print('No')