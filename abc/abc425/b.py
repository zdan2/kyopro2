n=int(input())
a=list(map(int,input().split()))
b=set(range(1,n+1))
sa=set(a)
sa.discard(-1)
sb=b^sa
for i in range(n):
    if a[i]==-1:
        a[i]=sb.pop()
if sb:
    print('No')
else:
    print('Yes')
    print(*a)