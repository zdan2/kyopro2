n=int(input())
for _ in range(n):
    a,b,c=map(int,input().split())
    if a==c and b==0:
        print(min(a,c)-1)
    else:
        print(min(a,c))