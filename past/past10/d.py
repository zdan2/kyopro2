t,n=map(int,input().split())
mx=[list(map(int,input().split())) for _ in range(t)]
for i in range(1,t+1):
    a=0
    for r in zip(*mx[:i]):
        a+=max(r)
    print(a)