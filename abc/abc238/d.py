n=int(input())
for _ in range(n):
    a,b=map(int,input().split())
    if b<a:
        print('No')
    elif (b-a)&a==a:
        print('Yes')
    else:
        print('No')