t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    c=0
    for _ in range(m):
        a,b=map(int,input().split())
        c=max(c,b-a+1)
    print(*[i%c+1 for i in range(n)])