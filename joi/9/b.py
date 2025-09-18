n,m=map(int,input().split())
r=[int(input()) for _ in range(n)]
x=0
c=[]
for i in range(m):
    d=int(input())
    x+=d
    x1=x
    if x<n:
        x+=r[x]
        x2=x
    if x1>=n-1 or x2>=n-1:
        print(i+1)
        exit()