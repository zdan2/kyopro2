n,q=map(int,input().split())
a=list(range(1,n+1))
r=0
for _ in range(q):
    b=list(map(int,input().split()))
    if b[0]==1:
        p=b[1]
        x=b[2]
        a[(r+p-1)%n]=x
    elif b[0]==2:
        p=b[1]
        print(a[(r+p-1)%n])
    else:
        r+=b[1]
        r%=n