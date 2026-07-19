n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]
b=[list(map(int,input().split())) for _ in range(n)]
a=sorted(a,key=lambda x:[x[0],x[1]])
b=sorted(b,key=lambda x:[x[0],x[1]])
c=[True]*n
for i in range(n):
    xa,xb=b[i]
    can=-1
    mb=-1
    for j in range(n-1,-1,-1):
        ya,yb=a[j]
        if ya<xa and yb<xb and c[j]:
            if yb>mb:
                can=j
                mb=yb
    if mb!=-1:
        c[can]=False
print(n-sum(c))