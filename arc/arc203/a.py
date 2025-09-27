t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    print(m+(n-2)*(m//2))