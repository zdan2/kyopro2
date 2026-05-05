n,m=map(int,input().split())
lr=[tuple(map(int,input().split())) for _ in range(n)]
lr.sort(key=lambda x:[x[1],x[1]-x[0]])
idx=0
cl=lr[idx][0]
cr=lr[idx][1]
l=1
c=0
for r in range(m+1):
    if l<=cl and r>=cr:
        while idx<n and l<=cl and r>=cr:
            idx+=1
            cl=lr[idx][0]
            cr=lr[idx][1]
    else:
        c+=r-l+1
print(c)