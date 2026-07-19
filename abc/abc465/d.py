t=int(input())
for _ in range(t):
    x,y,k=map(int,input().split())
    def f(x,y):
        if x==y:
            return 0
        if x<y:
            return 1+f(x,y//k)
        if x>y:
            return 1+f(x//k,y)
    print(f(x,y))