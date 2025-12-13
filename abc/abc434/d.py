n=int(input())
clouds=[]
h=0
w=0
for _ in range(n):
    cloud=list(map(int,input().split()))
    h=max(h,cloud[1])
    w=max(w,cloud[-1])
    clouds.append(cloud)
imos=[[0]*(w+1) for _ in range((h+1))]
def f (u,d,l,r):
    imos[u-1][l-1]+=1
    imos[u-1][r]-=1
    imos[d][l-1]-=1
    imos[d][r]+=1
for u,d,l,r in clouds:
    f(u,d,l,r)
def g(h,w):
    for y in range(h+1):
        for x in range(1,w+1):
            imos[y][x]+=imos[y][x-1]
    for x in range(w+1):
        for y in range(1,h+1):
            imos[y][x]+=imos[y-1][x]
g(h,w)
c=0
for r in imos:
    print(r)
for y in range(h):
    for x in range(w):
        if imos[y][x]==1:
            imos[y][x]=0
        elif imos[y][x]>1:
            imos[y][x]=1
        else:
            c+=1
pre_c=2000*2000-(h*w-c)
print(pre_c)
g(h,w)

for u,d,l,r in clouds:
    print(pre_c-(r-l+1)*(d-u+1)+(imos[d][r]-imos[u-1][r]-imos[d][l-1]+imos[u-1][r-1]))