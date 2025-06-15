n,t,q=map(int,input().split())
r=[]
for _ in range(n):
    a,b=map(int,input().split())
    if b==2:
        b=-1
    r.append((a,a+t*b,b))
x=[int(input()) for _ in range(q)]
for i in range(n-1):
    if r[i][1]>r[i+1][1] and r[i][2]!=r[i+1][2]:
        g=(r[i][0]+r[i+1][0])//2
        r[i]=(r[i][0],g,r[i][2])
        r[i+1]=(r[i+1][0],g,r[i+1][2])
for i in range(1,n):
    if r[i][2]==-1:
        if r[i-1][1]>r[i][1]:
            r[i]=(r[i][0],r[i-1][1],r[i][2])
for i in range(n-1,0,-1):
    if r[i][2]==1:
        if r[i][1]<r[i-1][1]:
            r[i-1]=(r[i-1][0],r[i][1],r[i-1][2])
for e in x:
    print(r[e-1][1])