n,s=map(int,input().split())
a=[0]+list(map(int,input().split()))
p=a[0]
for e in a[1:]:
    if e-p>s:
        print('No')
        exit()
    p=e
print('Yes')    