n,q=map(int,input().split())
a=list(map(int,input().split()))
a+=a
ca=[0]
for i in range(2*n):
    ca.append(ca[-1]+a[i])
s=0
for _ in range(q):
    b=list(map(int,input().split()))
    if b[0]==1:
        s=(s+b[1])%n
    if b[0]==2:
        i=b[1]-1
        j=b[2]-1
        l=s+i
        r=s+j
        res=ca[r+1]-ca[l] 
        print(res)       