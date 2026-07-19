n,l,r=map(int,input().split())
a=list(map(int,input().split()))
b=[a[0]]
for e in a[1:]:
    b.append(b[-1]+e)
mr=[]
for i in range(n):
    mr.append(b[i]-r*i)
m=mr[-1]
for i in range(n-2,-1,-1):
    if mr[i]>m:
        mr[i]=m
    if mr[i]<m:
        m=mr[i]
c=float('inf')
for i in range(n):
    c=min(c,l*i-b[i]+mr[i]+r*n)
print(c)