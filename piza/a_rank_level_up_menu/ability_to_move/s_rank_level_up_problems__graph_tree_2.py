n,m=map(int,input().split())
score=[0]*(n+1)
parent=[i for i in range(n+1)]
for i in range(1,n+1):
    a,p=map(int,input().split())
    score[i]=a
    parent[i]=p
    while True:
        score[p]+=a
        if p==0:
            break
        p=parent[p]
for _ in range(m):
    i=int(input())
    print(score[i])