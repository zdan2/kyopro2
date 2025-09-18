n,k=map(int,input().split())
a=sorted(set(map(int,input().split())))
for i in range(len(a)-k+1):
    if a[i+k-1]==a[i]+k-1:
        print('Yes')
        break
else:
    print('No')