n,m=map(int,input().split())
x=list(map(int,input().split()))
a=list(map(int,input().split()))
if sum(a)!=n:
    print(-1)
    exit()
c=0
s=[]
for i in range(m-1,-1,-1):
    xe=x[i]
    ae=a[i]
    if ae==1:
        s+=1     
    f=n-xe-ae+1
    l=n-xe
    if f<0:
        print(-1)
        exit()
    c+=(f+l)*ae//2
    n-=ae
    print(xe,ae,(f+l)*ae//2,n)
    if n<xe-1:
       print(-1)
       exit()
print(c) 