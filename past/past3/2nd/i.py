n=int(input())
q=int(input())
r=[0,0]
r[0]=[i for i in range(n)]
r[1]=[i for i in range(n)]
h=0
c=[]
for _ in range(q):
    z=list(map(int,input().split()))
    if z[0]==1:
        r[h][z[1]-1],r[h][z[2]-1]=r[h][z[2]-1],r[h][z[1]-1]
    if z[0]==2:
        hh=(h+1)%2
        r[hh][z[1]-1],r[hh][z[2]-1]=r[hh][z[2]-1],r[hh][z[1]-1]
    if z[0]==3:
        h=(h+1)%2
    if z[0]==4:
        if h==0:
            y=r[0][z[1]-1]
            x=r[1][z[2]-1]
        else:
            y=r[0][z[2]-1]
            x=r[1][z[1]-1]
        print(y*n+x)