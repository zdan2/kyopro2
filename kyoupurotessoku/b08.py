n=int(input())

mx=[[0]*1501 for _ in range(1501)]
mmx=[[0]*1501 for _ in range(1501)]

for _ in range(n):
    x,y=map(int,input().split())
    mx[x-1][y]+=1
    mx[x][y-1]+=1
    
for i in range(1500):
    for j in range(1500):
        mmx[i+1][j+1]=mmx[i][j+1]+mmx[i+1][j]-mmx[i][j]+mx[i][j]
        
m=int(input())
for _ in range(m):
    a,b,c,d=map(int,input().split())
    r=mmx[c][d]-mmx[a][d]-mmx[c][b]+mmx[a][b]
    print(r)