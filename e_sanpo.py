n,q=map(int,input().split())
mod=1000000007
a=list(map(int,input().split()))
c=list(map(int,input().split()))
c=[1]+c+[1]
r=0
for i in range(q+1):
    s=min(c[i],c[i+1])-1
    g=max(c[i],c[i+1])-1
    for j in range(s,g):
        r+=pow(a[j],a[j+1],mod) 
print(r)   