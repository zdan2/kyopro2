m,n=map(int,input().split())
s={i for i in range(1,n+1)}
for _ in range(m):
    k=int(input())
    a=list(map(int,input().split()))
    for i in range(k):
        if a[i] in s:
            s.remove(a[i])
            print(a[i])
            break
    else:
        print(0)