input()
a=list(map(int,input().split()))
for i,e in enumerate(map(int,input().split())):
    if i+1!=a[e-1]:
        print('No')
        exit()
print('Yes')